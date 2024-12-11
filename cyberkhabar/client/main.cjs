// main.cjs

const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
    // Create the browser window.
    const mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
           // preload: path.join(__dirname, 'preload.cjs'), // Optional: preload script
            contextIsolation: true, // Recommended for security
            enableRemoteModule: false, // Disable remote module
        },
    });

    // Load your HTML file or URL
    mainWindow.loadFile('index.html'); 
    
    
}

// This method will be called when Electron has finished initialization
app.whenReady().then(createWindow);

// Quit when all windows are closed, except on macOS
app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

// On macOS, create a new window in the app when the dock icon is clicked
app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});