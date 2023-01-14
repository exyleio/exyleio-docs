# Setting up

1. Clone the Exyle.io master repository

   ```
   git clone https://github.com/exyleio/exyleio.git
   ```

2. Install the following:

   - Python 3.10+
   - Node.js v18+
   - Docker CLI, Docker Engine, and Docker Compose
     (installing Docker Desktop installs everything for you)

3. Clone other repositories

   ```
   ./tool.py clone
   ```

   Your directory structure should now look something like this:

   ```
   exyleio/
   ├── ...
   ├── exyleio-.../
   ├── ...
   ├── tool.py
   └── docker-compose.yml
   ```

4. Run a project

   Example:

   ```
   ./tool.py run docs
   ```
