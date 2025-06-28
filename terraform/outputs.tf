
output "api_url" {
  value = azurerm_app_service.api.default_site_hostname
}

output "ui_url" {
  value = azurerm_app_service.ui.default_site_hostname
}
