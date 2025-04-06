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
    # Dynamically import the transformer module to avoid linter issues with cookiecutter templates
    pkg_name = __name__.split('.')[0]
    transformer_module = importlib.import_module(f"{pkg_name}.transformer")
    Transformer = transformer_module.Transformer
    
    logger.info(f"Infer called with document: {document.uuid}")

    # We can also get the pipeline context
    logger.info(f"Pipeline Context: {pipeline_context}")

    logger.info(f"Project: {project.name}")

    document_family = pipeline_context.document_family
    if document_family is not None:
        logger.info(f"Document Family: {document_family.path}")

    # Initialize and apply the transformer
    transformer_options = pipeline_context.parameters.get('transformer_options', {})
    transformer = Transformer(options=transformer_options)
    
    # Apply the transformation
    transformed_document = transformer.transform(document)
    
    logger.info(f"Document successfully transformed: {transformed_document.uuid}")

    # We also have a client configured
    client = KodexaClient()
    # Get model reference dynamically from the package name
    model_ref = f"{pipeline_context.parameters.get('org_slug', 'my-org')}/{pipeline_context.parameters.get('project_slug', pkg_name)}"
    logger.info(f"Get Model Name from Client: {client.get_object_by_ref('store', model_ref).name}")

    # We can also get the assistant
    logger.info(f"Assistant: {assistant}")

    return transformed_document
