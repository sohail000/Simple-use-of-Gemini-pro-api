import google.generativeai as genai
from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass
class GeminiConfig:
    temperature: float = 0.7
    max_output_tokens: int = 100
    top_p: float = 0.8
    top_k: int = 40
    
class GeminiAdapter:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = None
        self.current_config = None
        
    def setup_model(self, config: Optional[GeminiConfig] = None):
        if config is None:
            config = GeminiConfig()
            
        self.current_config = config
        generation_config = genai.types.GenerationConfig(
            temperature=config.temperature,
            max_output_tokens=config.max_output_tokens,
            top_p=config.top_p,
            top_k=config.top_k
        )
        
        self.model = genai.GenerativeModel(
            'gemini-pro',
            generation_config=generation_config
        )
        
    def generate_response(self, prompt: str) -> str:
        if self.model is None:
            self.setup_model()
            
        response = self.model.generate_content(prompt)
        return response.text
    
    def get_current_temperature(self) -> float:
        return self.current_config.temperature if self.current_config else 0.7
    
    def get_current_max_tokens(self) -> int:
        return self.current_config.max_output_tokens if self.current_config else 100