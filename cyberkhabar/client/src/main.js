import { createApp } from "vue";
import App from "./App.vue";
import "./style.css";
const app = createApp(App);
app.mount("#app");
const { eapp, BrowserWindow } = require('electron');
const path = require('path');
const isDev = require('electron-is-dev');

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: false,
      nodeIntegration: true,
    },
  });

  mainWindow.loadURL(
    isDev
      ? 'http://localhost:3000'
      : `file://${path.join(__dirname, 'dist/index.html')}`
  );

  if (isDev) {
    mainWindow.webContents.openDevTools();
  }

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

eapp.on('ready', createWindow);

eapp.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    eapp.quit();
  }
});

eapp.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});
