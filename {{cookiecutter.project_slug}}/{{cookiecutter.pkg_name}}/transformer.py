"""Transformer module."""

from kodexa import Document
import logging
import importlib
from typing import List
from kodexa.dataclasses import KodexaDocumentLLMWrapper
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Transformer:
    """
    A Kodexa transformer that processes documents and transforms their content.
    """

    def process_document(self, document: Document, assistant):
        external_data = document.get_external_data()
        try:
            # Clean up the labels/tags
            tagged_nodes = document.select('//word[hasTag()]')
            for node in tagged_nodes:
                [node.remove_tag(tag) for tag in node.get_tags() if tag in node.get_tags()]

            # Import the data_classes module
            from . import data_classes
            from kodexa.model.model import ContentException

            # Go through the external data and dynamically create instances
            data_objects = []

            for class_name, instances in external_data.items():
                if hasattr(data_classes, class_name):
                    DataClass = getattr(data_classes, class_name)
                    for instance in instances:
                        data_objects.append(DataClass(**instance))
                else:
                    logger.warning(f"Class {class_name} not found in data_classes module")

            logger.info(f"Found {len(data_objects)} data objects")

            # Implement the logic to transform the data objects

            transformed_objects = []
            for obj in data_objects:
                transformed_objects.append(obj)

            # Label the document based on the transformed objects
            llm_document_wrapper = KodexaDocumentLLMWrapper(document)
            for obj in transformed_objects:
                obj.apply_labels(llm_document_wrapper, assistant=assistant)

        except ImportError as e:
            error_message = f"Failed to import modules: {e}"
            logger.error(error_message)
            document.add_exception(ContentException("Invalid Document", error_message))
        except AttributeError as e:
            error_message = f"Required classes or functions not found: {e}"
            logger.error(error_message)
            document.add_exception(ContentException("Invalid Document", error_message))
        except Exception as e:
            error_message = f"An unexpected error occurred: {e}"
            logger.error(error_message)
            document.add_exception(ContentException("Processing Error", error_message))

        return document