# Overview

## Introduction

This is the documentation for the
[exyleio-deploy](https://github.com/exyleio/exyleio-deploy)
repository.

It is used to deploy and manage Exyle.io related services.

## Getting started

### Master server

1. Create an AWS EC2 instance and open terminal in it

2. Clone the repository **in the home directory** (important) and open it

   ```
   git clone https://github.com/exyleio/exyleio-deploy.git
   ```

   ```
   cd exyleio-deploy
   ```

3. Navigate to the `master-server` directory

   ```
   cd master-server
   ```

4. Create `.env` file

   - Check [Discord Bot Setup Guide](/docs/projects/discord-bot/overview#getting-started) for
     more information.

   ```dosini
   DISCORD_BOT_TOKEN=<DISCORD_BOT_TOKEN>
   DISCORD_BOT_ID=<DISCORD_BOT_ID>
   ```

5. Create a firebase project if you haven't already,
   [generate](https://console.firebase.google.com/u/0/project/_/settings/serviceaccounts/adminsdk)
   and download a service account key as `serviceAccountKey.json`.
   Beware, **THIS FILE MUST REMAIN PRIVATE**.

6. Run setup command

   ```
   ./tool.sh setup
   ```

7. Start the docker containers

   - this is the same command you use to update the master server
   - This will run the following:
     - redis database
     - discord bot
     - website (port 3000)
     - API server (port 8000)

   ```
   ./tool.sh restart
   ```

8. Setup routing

   - guide: https://www.youtube.com/watch?v=JQP96EjRM98

   Structure:

   ```mermaid
   %%{
      init: {
         "flowchart": {
               "curve": "linear"
         }
      }
   }%%

   flowchart LR
      user[User]
      user --- api-route
      user --- web-route

      subgraph aws[AWS]
         acm[Amazon Certificate Manager]

         subgraph route53[Route53]
            api-route[API Route]
            web-route[Website Route]
         end
         api-route --- api-balancer
         web-route --- web-balancer

         subgraph load-balancers[Load Balancers]
            api-balancer["API Load Balancer\nredirect HTTP:80 to HTTPS:443"]
            web-balancer[Website Load Balancer\nredirect HTTP:80 to HTTPS:443]
         end
         api-balancer --- api-target-group
         web-balancer --- web-target-group

         subgraph ec2[EC2]
            subgraph target-groups[Target Groups]
               api-target-group["API (port 8000)"]
               web-target-group["Website (port 3000)"]
            end
            master-server[Master Server]
         end
         target-groups --- master-server
      end
      acm --- load-balancers
   ```

## Learning

Minimum required skills to contribute to this project:

- GitHub action
- AWS
- Docker
