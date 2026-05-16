// APIM を除いたハンズオン用シンプル版 main.bicep
// 含むリソース: Resource Group / Log Analytics / Container Registry / Container Apps Environment
//             / Container App (TODO API) / Container App (MCP Server) / Static Web App

targetScope = 'subscription'

@minLength(1)
@maxLength(64)
@description('リソースグループおよびリソースの命名に使用する環境名')
param environmentName string

@minLength(1)
@description('リソースをデプロイするリージョン')
param location string

@description('Container App のコンテナイメージ（azd deploy で上書きされる）')
param apiImageName string = ''

@description('MCP サーバーのコンテナイメージ（azd deploy で上書きされる）')
param mcpImageName string = ''

var abbrs = loadJsonContent('./abbreviations.json')
var resourceToken = toLower(uniqueString(subscription().id, environmentName, location))
var tags = {
  'azd-env-name': environmentName
}

// リソースグループ
resource rg 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  name: '${abbrs.resourcesResourceGroups}${environmentName}'
  location: location
  tags: tags
}

// Log Analytics ワークスペース
module logAnalytics './modules/log-analytics.bicep' = {
  name: 'log-analytics'
  scope: rg
  params: {
    name: '${abbrs.operationalInsightsWorkspaces}${resourceToken}'
    location: location
    tags: tags
  }
}

// Container Registry
module containerRegistry './modules/container-registry.bicep' = {
  name: 'container-registry'
  scope: rg
  params: {
    name: '${abbrs.containerRegistryRegistries}${resourceToken}'
    location: location
    tags: tags
  }
}

// Container Apps 環境
module containerAppsEnvironment './modules/container-apps-environment.bicep' = {
  name: 'container-apps-environment'
  scope: rg
  params: {
    name: '${abbrs.appManagedEnvironments}${resourceToken}'
    location: location
    tags: tags
    logAnalyticsWorkspaceId: logAnalytics.outputs.id
  }
}

// Container App (TODO API)
module containerApp './modules/container-app.bicep' = {
  name: 'container-app'
  scope: rg
  params: {
    name: '${abbrs.appContainerApps}${resourceToken}'
    location: location
    tags: tags
    environmentId: containerAppsEnvironment.outputs.id
    containerRegistryName: containerRegistry.outputs.name
    containerRegistryLoginServer: containerRegistry.outputs.loginServer
    imageName: !empty(apiImageName) ? apiImageName : 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
    targetPort: 8000
  }
}

// Container App (TODO MCP Server)
module mcpContainerApp './modules/mcp-container-app.bicep' = {
  name: 'mcp-container-app'
  scope: rg
  params: {
    name: '${abbrs.appContainerApps}mcp-${resourceToken}'
    location: location
    tags: tags
    environmentId: containerAppsEnvironment.outputs.id
    containerRegistryName: containerRegistry.outputs.name
    containerRegistryLoginServer: containerRegistry.outputs.loginServer
    imageName: !empty(mcpImageName) ? mcpImageName : 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest'
    targetPort: 8080
    todoApiUrl: containerApp.outputs.uri
  }
}

// Static Web App (フロントエンド)
// Free プランは japaneast 非対応のため eastasia を使用
module staticWebApp './modules/static-web-app.bicep' = {
  name: 'static-web-app'
  scope: rg
  params: {
    name: '${abbrs.staticWebApp}${resourceToken}'
    location: 'eastasia'
    tags: tags
  }
}

// azd が参照する出力
output AZURE_CONTAINER_REGISTRY_ENDPOINT string = containerRegistry.outputs.loginServer
output AZURE_CONTAINER_REGISTRY_NAME string = containerRegistry.outputs.name
output AZURE_CONTAINER_APPS_ENVIRONMENT_ID string = containerAppsEnvironment.outputs.id
output AZURE_CONTAINER_APP_FQDN string = containerApp.outputs.fqdn
output AZURE_CONTAINER_APP_URI string = containerApp.outputs.uri
output AZURE_MCP_CONTAINER_APP_FQDN string = mcpContainerApp.outputs.fqdn
output AZURE_MCP_CONTAINER_APP_URI string = mcpContainerApp.outputs.uri
output AZURE_MCP_ENDPOINT string = '${mcpContainerApp.outputs.uri}/mcp'
output STATIC_WEB_APP_URI string = staticWebApp.outputs.uri
