import os
from crewai import Crew, Agent, Task, Process

# Configuration des agents métiers
AGENTS_CONFIG = {
    "intention_manager": {
        "role": "Gestionnaire d'intention",
        "goal": "Analyser et classifier les demandes utilisateur",
        "backstory": "Expert en analyse sémantique et classification d'intentions",
        "tools": ["semantic_analyzer", "intent_classifier"]
    },
    
    "functional_pm": {
        "role": "Chef de projet fonctionnel", 
        "goal": "Traduire les besoins métier en spécifications fonctionnelles",
        "backstory": "Chef de projet expérimenté en gestion de produit SaaS",
        "tools": ["requirement_analyzer", "functional_spec_generator"]
    },
    
    "technical_pm": {
        "role": "Chef de projet technique",
        "goal": "Définir l'architecture et les solutions techniques",
        "backstory": "Architecte solution avec expertise en systèmes distribués",
        "tools": ["architecture_designer", "tech_spec_generator"]
    },
    
    "lead_developer": {
        "role": "Lead développeur",
        "goal": "Implémenter les solutions avec les meilleures pratiques",
        "backstory": "Développeur senior expert en stack moderne",
        "tools": ["code_generator", "quality_checker"]
    },
    
    "release_manager": {
        "role": "Release manager",
        "goal": "Orchestrer les déploiements et la livraison continue",
        "backstory": "Expert DevOps en automatisation et déploiement",
        "tools": ["deployment_orchestrator", "quality_gate"]
    }
}

# Configuration des workflows
WORKFLOW_CONFIG = {
    "okr_evaluation": {
        "threshold": 0.85,
        "max_iterations": 5,
        "quality_metrics": ["precision", "completeness", "actionability"]
    }
}
