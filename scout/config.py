from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    amazon_client_id: str = os.getenv("AMAZON_SP_CLIENT_ID", "")
    amazon_client_secret: str = os.getenv("AMAZON_SP_CLIENT_SECRET", "")
    amazon_refresh_token: str = os.getenv("AMAZON_REFRESH_TOKEN", "")
    keepa_api_key: str = os.getenv("KEEPA_API_KEY", "")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")

    @property
    def amazon_configured(self) -> bool:
        return all((self.amazon_client_id, self.amazon_client_secret, self.amazon_refresh_token))

    @property
    def keepa_configured(self) -> bool:
        return bool(self.keepa_api_key)

    @property
    def ai_configured(self) -> bool:
        return bool(self.openai_api_key)


settings = Settings()
