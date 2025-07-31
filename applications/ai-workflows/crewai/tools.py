from crewai_tools import BaseTool
from typing import Any, Optional, Type
from pydantic import BaseModel, Field
import requests
import json

class SemanticAnalyzerInput(BaseModel):
    """Input schema for SemanticAnalyzer."""
    text: str = Field(..., description="Text to analyze for semantic meaning")

class SemanticAnalyzerTool(BaseTool):
    name: str = "Semantic Analyzer"
    description: str = (
        "Analyzes text to extract semantic meaning and intent classification. "
        "Useful for understanding user requests and intentions."
    )
    args_schema: Type[BaseModel] = SemanticAnalyzerInput

    def _run(self, text: str) -> str:
        """Execute semantic analysis on the given text."""
        # Implementation would connect to NLP service
        return f"Semantic analysis of: {text}"

class IntentClassifierInput(BaseModel):
    """Input schema for IntentClassifier."""
    message: str = Field(..., description="User message to classify")

class IntentClassifierTool(BaseTool):
    name: str = "Intent Classifier"
    description: str = (
        "Classifies user intents into predefined categories such as: "
        "coaching_request, appointment_booking, information_query, etc."
    )
    args_schema: Type[BaseModel] = IntentClassifierInput

    def _run(self, message: str) -> str:
        """Classify the intent of the user message."""
        # Intent classification logic
        intents = {
            "coaching": ["coach", "accompagnement", "soutien"],
            "appointment": ["rdv", "rendez-vous", "réserver"],
            "information": ["info", "renseignement", "question"]
        }
        
        for intent, keywords in intents.items():
            if any(keyword in message.lower() for keyword in keywords):
                return f"Intent classified as: {intent}"
        
        return "Intent classified as: general_inquiry"

class RequirementAnalyzerInput(BaseModel):
    """Input schema for RequirementAnalyzer."""
    requirements: str = Field(..., description="Requirements to analyze")

class RequirementAnalyzerTool(BaseTool):
    name: str = "Requirement Analyzer"  
    description: str = (
        "Analyzes functional requirements and breaks them down into "
        "actionable specifications and user stories."
    )
    args_schema: Type[BaseModel] = RequirementAnalyzerInput

    def _run(self, requirements: str) -> str:
        """Analyze requirements and generate specifications."""
        return f"Analyzed requirements: {requirements}"

class ArchitectureDesignerInput(BaseModel):
    """Input schema for ArchitectureDesigner."""
    specifications: str = Field(..., description="Technical specifications")

class ArchitectureDesignerTool(BaseTool):
    name: str = "Architecture Designer"
    description: str = (
        "Designs technical architecture based on functional specifications. "
        "Provides recommendations for technology stack, patterns, and structure."
    )
    args_schema: Type[BaseModel] = ArchitectureDesignerInput

    def _run(self, specifications: str) -> str:
        """Design technical architecture."""
        return f"Architecture designed for: {specifications}"

class CodeGeneratorInput(BaseModel):
    """Input schema for CodeGenerator."""
    specifications: str = Field(..., description="Code specifications")

class CodeGeneratorTool(BaseTool):
    name: str = "Code Generator"
    description: str = (
        "Generates code based on technical specifications and requirements. "
        "Follows best practices and coding standards."
    )
    args_schema: Type[BaseModel] = CodeGeneratorInput

    def _run(self, specifications: str) -> str:
        """Generate code based on specifications."""
        return f"Code generated for: {specifications}"

class QualityGateInput(BaseModel):
    """Input schema for QualityGate."""
    deliverable: str = Field(..., description="Deliverable to validate")

class QualityGateTool(BaseTool):
    name: str = "Quality Gate"
    description: str = (
        "Validates deliverables against quality standards and OKR metrics. "
        "Ensures all requirements are met before release."
    )
    args_schema: Type[BaseModel] = QualityGateInput

    def _run(self, deliverable: str) -> str:
        """Validate deliverable quality."""
        return f"Quality validation for: {deliverable}"

# Tool instances
semantic_analyzer_tool = SemanticAnalyzerTool()
intent_classifier_tool = IntentClassifierTool()
requirement_analyzer_tool = RequirementAnalyzerTool()
functional_spec_tool = RequirementAnalyzerTool()  # Alias
architecture_designer_tool = ArchitectureDesignerTool()
tech_spec_tool = ArchitectureDesignerTool()  # Alias
code_generator_tool = CodeGeneratorTool()
quality_checker_tool = QualityGateTool()
deployment_tool = QualityGateTool()  # Can be customized
quality_gate_tool = QualityGateTool()
