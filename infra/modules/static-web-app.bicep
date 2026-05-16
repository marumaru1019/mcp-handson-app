@description('Static Web App 名')
param name string

@description('デプロイリージョン')
param location string

@description('リソースタグ')
param tags object = {}

resource staticWebApp 'Microsoft.Web/staticSites@2024-04-01' = {
  name: name
  location: location
  tags: union(tags, { 'azd-service-name': 'web' })
  sku: {
    name: 'Free'
    tier: 'Free'
  }
  properties: {
    stagingEnvironmentPolicy: 'Enabled'
    allowConfigFileUpdates: true
  }
}

output id string = staticWebApp.id
output name string = staticWebApp.name
output uri string = 'https://${staticWebApp.properties.defaultHostname}'
output defaultHostname string = staticWebApp.properties.defaultHostname
