
## Run the Script

You can run the pre-population script using either the **psql command-line tool** or the **pgAdmin 4 application**.

---

### Option 1: Using the psql Command-Line

This method is fast and efficient if you're comfortable with the terminal.

#### 🔧 Prerequisites: Installing `psql`

The `psql` command-line tool is part of the PostgreSQL client package. If you don't have it installed, here’s how to get it:

* **Windows **: `psql` is included in the full PostgreSQL installer. Download it from the [official PostgreSQL website](https://www.postgresql.org/download/).

* **macOS ** (using [Homebrew](https://brew.sh)):

  ```bash
  brew install postgresql
  ```

* **Linux (Debian/Ubuntu) **:

  ```bash
  sudo apt-get update
  sudo apt-get install postgresql-client
  ```

---

#### ▶Execute the Script

From the project root (`ERRGO_BE`), run the following command:

```bash
psql -U postgres -d errgo -f pre-populate/pre-populate-env.sql
```

**Command breakdown:**

* `-U postgres` → Your PostgreSQL username (default: `postgres`)
* `-d errgo` → The name of your database
* `-f ...` → The file path to the SQL script

You will be prompted for your PostgreSQL password.

---

### Option 2: Using the pgAdmin 4 Application

This method is a great **visual alternative** if you prefer not to use the command line.

1. **Open pgAdmin 4** and connect to your server.
2. **Locate Your Database**: In the Object Explorer panel on the left, navigate to:
   `Servers → Your Server → Databases → errgo`
3. **Open the Query Tool**: Right-click the `errgo` database → **Query Tool**.
4. **Load the Script**: In the new Query Editor panel, click  **Open File** 
5. **Select the File**: Choose:

   ```
   pre-populate/pre-populate-env.sql
   ```
6. **Execute the Script**: Click the **Execute/Run icon**  in the toolbar.

