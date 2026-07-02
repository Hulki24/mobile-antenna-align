from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import (
    CONF_HOST,
    CONF_PASSWORD,
    CONF_USERNAME,
)

from .const import DOMAIN


class MobileAntennaAlignConfigFlow(
    config_entries.ConfigFlow,
    domain=DOMAIN,
):
    """Handle a config flow for Mobile Antenna Align."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""

        if user_input is not None:
            # TODO: Validate router connection before creating the entry.
            
            return self.async_create_entry(
                title=user_input[CONF_HOST],
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_HOST): str,
                    vol.Required(CONF_USERNAME): str,
                    vol.Required(CONF_PASSWORD): str,
                }
            ),
        )