"""Main module."""

from kodexa import Document, get_source, PipelineContext, KodexaClient, Assistant
from kodexa.platform.client import ProjectEndpoint, DocumentFamilyEndpoint
import logging
import importlib

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def infer(document: Document, project: ProjectEndpoint, pipeline_context: PipelineContext, assistant: Assistant):
    """
    Inference function that processes a document using the Transformer.
    
    Args:
        document (Document): The input Kodexa document
        project (ProjectEndpoint): The project endpoint
        pipeline_context (PipelineContext): The pipeline context
        assistant (Assistant): The assistant object
        
    Returns:
        Document: The transformed document
    """
    
    # Initialize and apply the transformer
    from .transformer import Transformer
    transformer = Transformer()
    return transformer.process_document(document, assistant)