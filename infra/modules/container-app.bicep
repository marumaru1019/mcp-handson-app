@description('Container App 名')
param name string

@description('デプロイリージョン')
param location string

@description('リソースタグ')
param tags object = {}

@description('Container Apps 環境のリソース ID')
param environmentId string

@description('Container Registry 名')
param containerRegistryName string

@description('Container Registry のログインサーバー')
param containerRegistryLoginServer string

@description('コンテナイメージ名')
param imageName string

@description('コンテナがリッスンするポート')
param targetPort int = 8000

@description('CORS で許可するオリジン（カンマ区切り）')
param allowedOrigins string = '*'

resource containerApp 'Microsoft.App/containerApps@2024-03-01' = {
  name: name
  location: location
  tags: union(tags, { 'azd-service-name': 'api' })
  properties: {
    managedEnvironmentId: environmentId
    configuration: {
      activeRevisionsMode: 'Single'
      ingress: {
        external: true
        targetPort: targetPort
        transport: 'auto'
        allowInsecure: false
      }
      registries: [
        {
          server: containerRegistryLoginServer
          username: containerRegistryName
          passwordSecretRef: 'registry-password'
        }
      ]
      secrets: [
        {
          name: 'registry-password'
          value: listCredentials(resourceId('Microsoft.ContainerRegistry/registries', containerRegistryName), '2023-11-01-preview').passwords[0].value
        }
      ]
    }
    template: {
      containers: [
        {
          name: 'todo-api'
          image: imageName
          resources: {
            cpu: json('0.5')
            memory: '1Gi'
          }
          env: [
            {
              name: 'DATABASE_URL'
              value: 'sqlite:///./todo.db'
            }
            {
              name: 'ALLOWED_ORIGINS'
              value: allowedOrigins
            }
          ]
        }
      ]
      scale: {
        minReplicas: 1
        maxReplicas: 3
        rules: [
          {
            name: 'http-scaling'
            http: {
              metadata: {
                concurrentRequests: '50'
              }
            }
          }
        ]
      }
    }
  }
}

output id string = containerApp.id
output name string = containerApp.name
output fqdn string = containerApp.properties.configuration.ingress.fqdn
output uri string = 'https://${containerApp.properties.configuration.ingress.fqdn}'
