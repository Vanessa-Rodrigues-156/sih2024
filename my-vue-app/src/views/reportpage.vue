<script>
import { ref } from 'vue';
export default {
    name: 'IncidentList',
    setup() {
        const incidents = ref([
            {
                id: 1,
                title: 'Data Breach at Major Indian Bank',
                description: 'A significant data breach has occurred at a major Indian bank, exposing sensitive customer information.',
                image: 'https://placehold.co/64x64',
                source: 'Bank Security News',
                date: '2023-10-01'
            },
            {
                id: 2,
                title: 'Ransomware Attack on Indian Healthcare System',
                description: 'A ransomware attack has disrupted operations at several hospitals across India, demanding a hefty ransom.',
                image: 'https://placehold.co/64x64',
                source: 'Healthcare Cyber Watch',
                date: '2023-10-02'
            },
            {
                id: 3,
                title: 'Phishing Scam Targets Indian Government Employees',
                description: 'A new phishing scam is targeting Indian government employees, attempting to steal login credentials.',
                image: 'https://placehold.co/64x64',
                source: 'Govt Cyber Alerts',
                date: '2023-10-03'
            },
            {
                id: 4,
                title: 'Cyber Attack on Indian Power Grid',
                description: 'A cyber attack has been reported on the Indian power grid, causing temporary outages in several regions.',
                image: 'https://placehold.co/64x64',
                source: 'Energy Sector News',
                date: '2023-10-04'
            },
            {
                id: 5,
                title: 'Malware Found in Popular Indian Mobile App',
                description: 'Malware has been discovered in a popular Indian mobile app, compromising user data and privacy.',
                image: 'https://placehold.co/64x64',
                source: 'Mobile Security News',
                date: '2023-10-05'
            },
            {
                id: 6,
                title: 'Cyber Espionage Campaign Targets Indian Defense Sector',
                description: 'A cyber espionage campaign has been detected targeting the Indian defense sector, aiming to steal sensitive information.',
                image: 'https://placehold.co/64x64',
                source: 'Defense Cyber Alerts',
                date: '2023-10-06'
            },
            {
                id: 7,
                title: 'Indian E-commerce Platform Suffers Data Breach',
                description: 'A data breach has occurred at a major Indian e-commerce platform, exposing customer payment information.',
                image: 'https://placehold.co/64x64',
                source: 'E-commerce Security News',
                date: '2023-10-07'
            },
            {
                id: 8,
                title: 'DDoS Attack on Indian Telecom Provider',
                description: 'A DDoS attack has disrupted services at a major Indian telecom provider, affecting millions of users.',
                image: 'https://placehold.co/64x64',
                source: 'Telecom Cyber Watch',
                date: '2023-10-08'
            },
            {
                id: 9,
                title: 'Indian Financial Institution Hit by Cyber Fraud',
                description: 'A cyber fraud incident has been reported at a major Indian financial institution, resulting in significant financial losses.',
                image: 'https://placehold.co/64x64',
                source: 'Financial Cyber Alerts',
                date: '2023-10-09'
            },
            {
                id: 10,
                title: 'Cyber Attack on Indian Educational Institutions',
                description: 'Several Indian educational institutions have been targeted in a cyber attack, compromising student and staff data.',
                image: 'https://placehold.co/64x64',
                source: 'Education Cyber News',
                date: '2023-10-10'
            },
            {
                id: 11,
                title: 'Indian Media Company Suffers Data Breach',
                description: 'A data breach has been reported at a major Indian media company, exposing sensitive information.',
                image: 'https://placehold.co/64x64',
                source: 'Media Security News',
                date: '2023-10-11'
            },
            {
                id: 12,
                title: 'Cyber Attack on Indian Transportation Network',
                description: 'A cyber attack has disrupted operations in the Indian transportation network, causing delays and cancellations.',
                image: 'https://placehold.co/64x64',
                source: 'Transport Cyber Alerts',
                date: '2023-10-12'
            },
            {
                id: 13,
                title: 'Indian Retail Chain Hit by Cyber Attack',
                description: 'A cyber attack has targeted a major Indian retail chain, compromising customer payment information.',
                image: 'https://placehold.co/64x64',
                source: 'Retail Cyber Watch',
                date: '2023-10-13'
            },
            {
                id: 14,
                title: 'Cyber Attack on Indian Manufacturing Sector',
                description: 'A cyber attack has been reported in the Indian manufacturing sector, disrupting production lines.',
                image: 'https://placehold.co/64x64',
                source: 'Manufacturing Cyber News',
                date: '2023-10-14'
            },
            {
                id: 15,
                title: 'Indian Government Website Defaced by Hackers',
                description: 'A major Indian government website has been defaced by hackers, displaying unauthorized content.',
                image: 'https://placehold.co/64x64',
                source: 'Govt Cyber Alerts',
                date: '2023-10-15'
            }
        ]);

        return {
            incidents
        };
    }
};
</script>

<template>
    <div class="container">
        <header>
            <h1>Cyber Incident Real-Time Feed</h1>
            <nav>
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">About</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
            </nav>
        </header>
        <main>
            <section class="mb-8">
                <h2 class="mb-4">Latest Cyber Incidents</h2>
                <div v-for="incident in incidents" :key="incident.id" class="incident-card mb-4">
                    <h3>{{ incident.title }}</h3>
                    <p class="description">{{ incident.description }}</p>
                    <div class="incident-info">
                        <img :src="incident.image" alt="Detailed description of the image" class="incident-image">
                        <div>
                            <p class="source">{{ incident.source }}</p>
                            <p class="date">{{ incident.date }}</p>
                        </div>
                    </div>
                </div>
            </section>
        </main>
    </div>
</template>

<style>
body {
    background-color: #f3f4f6;
}
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 1rem;
}

header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 0;
}

h1 {
    font-size: 1.875rem;
    font-weight: bold;
    color: #1f2937;
}

nav ul {
    display: flex;
    gap: 1rem;
}

nav a {
    color: #4b5563;
    text-decoration: none;
}

nav a:hover {
    color: #1f2937;
}

.mb-8 {
    margin-bottom: 2rem;
}

.mb-4 {
    margin-bottom: 1rem;
}

h2 {
    font-size: 1.5rem;
    font-weight: bold;
    color: #1f2937;
}

.incident-card {
    background-color: white;
    padding: 1rem;
    border-radius: 0.5rem;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

h3 {
    font-size: 1.25rem;
    font-weight: 600;
    color: #1f2937;
}

.description {
    color: #4b5563;
}

.incident-info {
    display: flex;
    align-items: center;
    margin-top: 0.5rem;
}

.incident-image {
    width: 4rem;
    height: 4rem;
    border-radius: 9999px;
    margin-right: 1rem;
}

.source {
    color: #1f2937;
    font-weight: 600;
}

.date {
    color: #4b5563;
    font-size: 0.875rem;
}
</style>