Run the Script
You can run the pre-population script using either the psql command-line tool or the pgAdmin 4 application.

Option 1: Using the psql Command-Line
This method is fast and efficient if you're comfortable with the terminal.

Prerequisites: Installing psql
The psql command-line tool is part of the PostgreSQL client package. If you don't have it installed, here’s how to get it:

Windows 🖥️: psql is included in the full PostgreSQL installer. Download it from the official PostgreSQL website.

macOS 🍎: The easiest way is using Homebrew.

Bash

brew install postgresql
Linux (Debian/Ubuntu) 🐧:

Bash

sudo apt-get update
sudo apt-get install postgresql-client
Execute the Script
From the project root (ERRGO_BE), run the following command:

Bash

psql -U postgres -d errgo -f pre-populate/pre-populate-env.sql
Command breakdown:

-U postgres → Your PostgreSQL username (default is postgres).

-d errgo → The name of your database.

-f ... → The file path to the SQL script.

You will be prompted for your PostgreSQL password.

Option 2: Using the pgAdmin 4 Application
This method is a great visual alternative if you prefer not to use the command line.

Open pgAdmin 4 and connect to your server.

Locate Your Database: In the Object Explorer panel on the left, navigate to Servers -> Your Server -> Databases -> errgo.

Open the Query Tool: Right-click on the errgo database and select Query Tool.

Load the Script: In the new Query Editor panel, click the Open File icon (looks like a folder) in the toolbar.

Select the File: Navigate to your project folder and select the pre-populate/pre-populate-env.sql script.

Execute the Script: Click the Execute/Refresh icon (looks like a lightning bolt ⚡) in the toolbar to run the entire script.

Verify Success: Look at the Messages tab in the bottom panel. You should see a success message, for example: Query returned successfully.
