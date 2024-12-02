const mongoose = require('mongoose');
const fs = require('fs');
const path = require('path');

// AWS DocumentDB Configuration
const ca = [fs.readFileSync(path.join(__dirname, 'rds-combined-ca-bundle.pem'))]

const dbConfig = {
    url: process.env.MONGODB_URL || 'mongodb://<username>:<password>@your-docdb-cluster.cluster-xxxxx.region.docdb.amazonaws.com:27017/cyberkhabar?tls=true&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false',
    options: {
        useNewUrlParser: true,
        useUnifiedTopology: true,
        ssl: true,
        sslValidate: true,
        sslCA: ca,
        retryWrites: false
    }
};

const connectDB = async () => {
    try {
        await mongoose.connect(dbConfig.url, dbConfig.options);
        console.log('Successfully connected to AWS DocumentDB');
    } catch (error) {
        console.error('Connection error:', error);
        process.exit(1);
    }
};

module.exports = connectDB;
