Populating the Database with Dummy Data
To facilitate frontend development and testing, a SQL script is provided to pre-populate your local database with a consistent set of mock data. This script creates users, projects, teams, and workspaces, ensuring you have a ready-to-use environment right after setup.

Prerequisites
Before running the script, ensure that:

You have successfully set up PostgreSQL on your local or WSL environment.

The PostgreSQL service is running.

You have created the errgo database and applied all the necessary Prisma migrations (npx prisma migrate dev).

1. Configure the Script
The provided SQL script needs a minor configuration to target the correct database schema.

Open the script file located at ERRGO_BE/pre-populate/pre-populate-env.sql.

Find the first line:

SET search_path TO 'schema_name';

Replace 'schema_name' with the name of your schema. If you are using the default PostgreSQL schema, this is typically 'public'. The line should look like this:

SET search_path TO 'public';

Save and close the file.

2. Run the Script
Execute the script using the psql command-line tool. This will connect to your database and run the commands in the file.

Open your terminal and navigate to the root directory of the project (ERRGO_BE).

Run the following command. You will be prompted for the password for your postgres user.

psql -U postgres -d errgo -f pre-populate/pre-populate-env.sql

-U postgres: Specifies the user (postgres).

-d errgo: Specifies the database name (errgo).

-f ...: Specifies the file to execute.

3. Verify the Data
After the script runs, the database will be populated. You can verify that the data was added successfully in a couple of ways:

Using Prisma Studio: This is the easiest way to see the data in a user-friendly interface.

npx prisma studio

Navigate through the models to see the newly created users, projects, etc.

Using psql: You can connect directly to the database and run SQL queries.

# Connect to the database
psql -U postgres -d errgo

# Run a query to see the new users
SELECT * FROM "users";

Your local environment is now populated with mock data, and you can proceed with frontend development and testing.
