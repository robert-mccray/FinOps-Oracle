provider "azurerm" {
  features {}
}

resource "azurerm_linux_virtual_machine" "expensive_dev_box" {
  name                = "dev-machine-01"
  resource_group_name = "rg-dev-environment"
  location            = "East US"
  size                = "Standard_E64s_v4" # 64 Cores, 504GB RAM. Massive overkill for dev.
  admin_username      = "adminuser"
  # ... network interfaces and os_disk omitted for brevity
}
