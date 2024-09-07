const { spawn } = require("child_process");

function startBotProcess(script, command = "node") {
    // Start a child process to run the script using the specified command
    const child = spawn(command, ["--trace-warnings", "--async-stack-traces", script], {
        cwd: __dirname,
        stdio: "inherit",
        shell: true
    });

    // Listen for the 'close' event to handle script exits
    child.on("close", (codeExit) => {
        console.log(`${script} process exited with code: ${codeExit}`);
        // If the exit code is non-zero, restart the process after 3 seconds
        if (codeExit !== 0) {
            setTimeout(() => startBotProcess(script, command), 3000);
        }
    });

    // Listen for the 'error' event to handle process errors
    child.on("error", (error) => {
        console.error(`An error occurred starting the ${script} process: ${error}`);
    });
}

// Start the bot process for the Node.js script first
startBotProcess("monitor.js");

// Start the bot process for the Python script after monitor.js
startBotProcess("system.py", "python"); // or use "python3" if needed
