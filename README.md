## ChatGPT-on-CMD

This repository allows you to interact with GPT-4o-mini directly from your command-line interface (CLI) on Windows. Follow this guide to set it up so you can run the chat client from anywhere.

### Prerequisites

- **Python 3.6+** installed on your machine
- **`openai` Python package**

### Clone the Repository

```cmd
git clone https://github.com/your-username/ChatGPT-on-CMD.git
cd ChatGPT-on-CMD
```

### Install Dependencies

```cmd
pip install openai
```

### Configuration

**Setting Environment Variables**

Set your API base URL and API key (if needed) using environment variables:

```cmd
set OPENAI_API_BASE=http://localhost:8000/v1
set OPENAI_API_KEY=your-local-api-key
```

*Skip `OPENAI_API_KEY` if not required by your setup.*

**Adding ChatGPT-on-CMD to Your PATH**

To make the ChatGPT-on-CMD command available from any directory, add the script's location to your system's PATH.

1. **Find the path to ChatGPT-on-CMD:**

   Navigate to the directory where you cloned the repo and copy the path from the address bar.

2. **Add the directory to PATH:**

   - Open System Properties → Environment Variables.
   - Under System variables, find Path, and click Edit.
   - Click New and paste the path to ChatGPT-on-CMD.
   - Click OK to save and close.

**Running the Chat Client Globally**

After adding ChatGPT-on-CMD to your PATH, you can use the following command from any directory:

```cmd
chatgpt.bat
```

Alternatively, if you want to run the .py file directly, create an alias using doskey:

Open Command Prompt and type:

```cmd
doskey chatgpt=python C:\path\to\ChatGPT-on-CMD\chatgpt.py $*
```

Now, you can run:

```cmd
chatgpt
```

*Note: The `doskey` command is session-based. To make it persistent, add it to your startup scripts or .bat files.*

### License

This project is licensed under the MIT License.