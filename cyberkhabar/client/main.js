import { app, BrowserWindow } from "electron";
import path from "path";
import isDev from "electron-is-dev";

function createWindow() {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    minWidth: 400, // Minimum width
    minHeight: 300, // Minimum height
    webPreferences: {
      contextIsolation: true, // Recommended for security
      enableRemoteModule: false, // Disable remote module
      // preload: path.join(__dirname, "preload.js"), // Optional: preload script
    },
  });

  if (isDev) {
    // Load the URL of the dev server if in development mode
    mainWindow.loadURL("http://localhost:5173/");
  } else {
    // Load the index.html file from the dist directory if in production mode
    mainWindow.loadFile(path.join(__dirname, "dist", "index.html"));
  }

  mainWindow.on("closed", () => {
    mainWindow = null;
  });

  // Handle window resizing
  mainWindow.on("resize", () => {
    const { width, height } = mainWindow.getBounds();
    console.log(`Window resized to ${width}x${height}`);
  });
}

app.on("ready", createWindow);

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});

app.on("activate", () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});
