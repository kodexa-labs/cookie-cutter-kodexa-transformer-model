"""Transformer module."""

from kodexa import Document, Content
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Transformer:
    """
    A Kodexa transformer that processes documents and transforms their content.
    """

    def __init__(self, options=None):
        """
        Initialize the transformer with optional configuration.
        
        Args:
            options (dict, optional): Configuration options for the transformer.
        """
        self.options = options if options else {}
        logger.info(f"Initialized transformer with options: {self.options}")

    def transform(self, document: Document) -> Document:
        """
        Transform the input document according to the transformer's logic.
        
        Args:
            document (Document): The input Kodexa document to transform
            
        Returns:
            Document: The transformed Kodexa document
        """
        logger.info(f"Transforming document: {document.uuid}")
        
        # Example transformation - add a label
        document.add_label("transformed")
        
        # Example: Extract some information from the document
        # You would replace this with your specific transformation logic
        if document.content_type == Content.ContentType.TEXT:
            text_content = document.content_as_string
            logger.info(f"Document content length: {len(text_content)} characters")
            
            # Example simple transformation (uppercase first 10 characters if available)
            if len(text_content) > 10:
                # This is just an example - replace with your actual transformation
                logger.info("Applying sample transformation")
        
        return document 