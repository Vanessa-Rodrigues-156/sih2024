<template>
  <div class="flex flex-col w-full min-h-screen bg-background">
    <header class="flex items-center h-16 px-4 border-b shrink-0 md:px-6">
      <a class="flex items-center gap-2 text-lg font-semibold sm:text-base mr-4" href="#">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
          class="w-6 h-6"
        >
          <path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"></path>
        </svg>
        <span>Cyber Incident Monitor</span>
      </a>
      <nav class="hidden font-medium sm:flex flex-row items-center gap-5 text-sm lg:gap-6">
        <a class="text-muted-foreground" href="#">Dashboard</a>
        <a class="text-muted-foreground" href="#">Incidents</a>
        <a class="text-muted-foreground" href="#">Alerts</a>
        <a class="text-muted-foreground" href="#">Integrations</a>
        <a class="text-muted-foreground" href="#">Settings</a>
      </nav>
      <div class="flex items-center w-full gap-4 md:ml-auto md:gap-2 lg:gap-4">
        <button class="inline-flex items-center justify-center gap-2 whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 [&amp;_svg]:pointer-events-none [&amp;_svg]:size-4 [&amp;_svg]:shrink-0 hover:bg-accent hover:text-accent-foreground h-10 w-10 rounded-full ml-auto">
          <img
            src="/placeholder.svg"
            width="32"
            height="32"
            class="rounded-full border"
            alt="Avatar"
            style="aspect-ratio:32/32;object-fit:cover"
          />
          <span class="sr-only">Toggle user menu</span>
        </button>
      </div>
    </header>
    <main class="flex min-h-[calc(100vh_-_theme(spacing.16))] flex-1 flex-col gap-4 p-4 md:gap-8 md:p-10">
      <div class="max-w-6xl w-full mx-auto grid gap-2">
        <h1 class="font-semibold text-3xl">Cyber Incident Monitor</h1>
        <div class="flex items-center text-sm gap-2">
          <div class="text-muted-foreground flex items-center gap-2">
            <span class="inline-block w-2 h-2 bg-[#09CE6B] rounded-full animate-ping duration-[5000]"></span>Real-time
            Monitoring
          </div>
        </div>
      </div>
      <div class="grid gap-6 max-w-6xl w-full mx-auto">
        <div>
          <div class="rounded-lg border bg-card text-card-foreground shadow-sm p-0 overflow-hidden" data-v0-t="card">
            <div class="flex flex-col space-y-1.5 p-6">
              <p class="text-muted-foreground text-sm font-medium">Cyber Incidents</p>
              <h3 class="font-semibold tracking-tight text-2xl">2,389</h3>
            </div>
            <div class="p-6 pt-0">
              <div class="aspect-[9/4]">
                <div style="width:100%;height:100%"></div>
              </div>
            </div>
          </div>
        </div>
        <div class="grid gap-6 lg:grid-cols-3">
          <!-- Incident Types Card -->
          <div class="rounded-lg border bg-card text-card-foreground shadow-sm relative overflow-hidden" data-v0-t="card">
            <div class="space-y-1.5 p-6 flex flex-row items-center border-b">
              <h3 class="text-2xl font-semibold leading-none tracking-tight">Incident Types</h3>
              <p class="text-sm text-muted-foreground ml-auto">Incidents</p>
            </div>
            <div class="grid gap-4 text-sm p-6">
              <div class="flex items-center">
                <div>Malware</div>
                <div class="font-semibold ml-auto">1.2K</div>
              </div>
              <div class="flex items-center">
                <div>Phishing</div>
                <div class="font-semibold ml-auto">1K</div>
              </div>
              <div class="flex items-center">
                <div>DDoS</div>
                <div class="font-semibold ml-auto">800</div>
              </div>
              <div class="flex items-center">
                <div>Data Breach</div>
                <div class="font-semibold ml-auto">650</div>
              </div>
              <div class="flex items-center">
                <div>Ransomware</div>
                <div class="font-semibold ml-auto">450</div>
              </div>
            </div>
            <div class="flex items-center p-6 pt-0 pb-4 px-6 justify-center bg-gradient-to-b from-background/50 to-background absolute inset-x-0 bottom-0">
              <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 [&amp;_svg]:pointer-events-none [&amp;_svg]:size-4 [&amp;_svg]:shrink-0 border border-input hover:bg-accent hover:text-accent-foreground h-9 px-3 gap-2 rounded-full bg-background">
                View All
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="w-4 h-4"
                >
                  <polyline points="15 3 21 3 21 9"></polyline>
                  <polyline points="9 21 3 21 3 15"></polyline>
                  <line x1="21" x2="14" y1="3" y2="10"></line>
                  <line x1="3" x2="10" y1="21" y2="14"></line>
                </svg>
              </button>
            </div>
          </div>
          <!-- Affected Sectors Card -->
          <div class="rounded-lg border bg-card text-card-foreground shadow-sm relative overflow-hidden" data-v0-t="card">
            <div class="space-y-1.5 p-6 flex flex-row items-center border-b">
              <h3 class="text-2xl font-semibold leading-none tracking-tight">Affected Sectors</h3>
              <p class="text-sm text-muted-foreground ml-auto">Incidents</p>
            </div>
            <div class="grid gap-4 text-sm p-6">
              <div class="flex items-center">
                <div>Government</div>
                <div class="font-semibold ml-auto">1.5K</div>
              </div>
              <div class="flex items-center">
                <div>Finance</div>
                <div class="font-semibold ml-auto">1.2K</div>
              </div>
              <div class="flex items-center">
                <div>Healthcare</div>
                <div class="font-semibold ml-auto">1K</div>
              </div>
              <div class="flex items-center">
                <div>Education</div>
                <div class="font-semibold ml-auto">800</div>
              </div>
              <div class="flex items-center">
                <div>Critical Infrastructure</div>
                <div class="font-semibold ml-auto">650</div>
              </div>
            </div>
            <div class="flex items-center p-6 pt-0 pb-4 px-6 justify-center bg-gradient-to-b from-background/50 to-background absolute inset-x-0 bottom-0">
              <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 [&amp;_svg]:pointer-events-none [&amp;_svg]:size-4 [&amp;_svg]:shrink-0 border border-input hover:bg-accent hover:text-accent-foreground h-9 px-3 gap-2 rounded-full bg-background">
                View All
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="w-4 h-4"
                >
                  <polyline points="15 3 21 3 21 9"></polyline>
                  <polyline points="9 21 3 21 3 15"></polyline>
                  <line x1="21" x2="14" y1="3" y2="10"></line>
                  <line x1="3" x2="10" y1="21" y2="14"></line>
                </svg>
              </button>
            </div>
          </div>
          <!-- Geographic Distribution Card -->
          <div class="rounded-lg border bg-card text-card-foreground shadow-sm relative overflow-hidden" data-v0-t="card">
            <div class="space-y-1.5 p-6 flex flex-row items-center border-b">
              <h3 class="text-2xl font-semibold leading-none tracking-tight">Geographic Distribution</h3>
              <p class="text-sm text-muted-foreground ml-auto">Incidents</p>
            </div>
            <div class="grid gap-4 text-sm p-6">
              <div class="flex items-center">
                <div>New Delhi</div>
                <div class="font-semibold ml-auto">1.2K</div>
              </div>
              <div class="flex items-center">
                <div>Mumbai</div>
                <div class="font-semibold ml-auto">1K</div>
              </div>
              <div class="flex items-center">
                <div>Bengaluru</div>
                <div class="font-semibold ml-auto">900</div>
              </div>
              <div class="flex items-center">
                <div>Chennai</div>
                <div class="font-semibold ml-auto">800</div>
              </div>
              <div class="flex items-center">
                <div>Hyderabad</div>
                <div class="font-semibold ml-auto">650</div>
              </div>
            </div>
            <div class="flex items-center p-6 pt-0 pb-4 px-6 justify-center bg-gradient-to-b from-background/50 to-background absolute inset-x-0 bottom-0">
              <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 [&amp;_svg]:pointer-events-none [&amp;_svg]:size-4 [&amp;_svg]:shrink-0 border border-input hover:bg-accent hover:text-accent-foreground h-9 px-3 gap-2 rounded-full bg-background">
                View All
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="w-4 h-4"
                >
                  <polyline points="15 3 21 3 21 9"></polyline>
                  <polyline points="9 21 3 21 3 15"></polyline>
                  <line x1="21" x2="14" y1="3" y2="10"></line>
                  <line x1="3" x2="10" y1="21" y2="14"></line>
                </svg>
              </button>
            </div>
          </div>
        </div>
        <div class="grid gap-6 lg:grid-cols-2">
          <!-- Recent Incidents Card -->
          <div class="rounded-lg border bg-card text-card-foreground shadow-sm relative overflow-hidden" data-v0-t="card">
            <div class="space-y-1.5 p-6 flex flex-row items-center border-b">
              <h3 class="text-2xl font-semibold leading-none tracking-tight">Recent Incidents</h3>
              <p class="text-sm text-muted-foreground ml-auto">
                <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 [&amp;_svg]:pointer-events-none [&amp;_svg]:size-4 [&amp;_svg]:shrink-0 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-9 rounded-md px-3 gap-2">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="w-4 h-4"
                  >
                    <polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"></polygon>
                  </svg>
                  Filter
                </button>
              </p>
            </div>
            <div class="grid gap-4 text-sm p-6">
              <div class="flex items-center">
                <div class="flex items-center gap-2">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="w-5 h-5 text-red-500"
                  >
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="12" x2="12" y1="8" y2="12"></line>
                    <line x1="12" x2="12.01" y1="16" y2="16"></line>
                  </svg>
                  <div>
                    <div class="font-medium">Ransomware Attack</div>
                    <div class="text-muted-foreground">Affected: Government Sector</div>
                  </div>
                </div>
                <div class="font-semibold ml-auto">2h ago</div>
              </div>
              <div class="flex items-center">
                <div class="flex items-center gap-2">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="w-5 h-5 text-yellow-500"
                  >
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="12" x2="12" y1="8" y2="12"></line>
                    <line x1="12" x2="12.01" y1="16" y2="16"></line>
                  </svg>
                  <div>
                    <div class="font-medium">Phishing Campaign</div>
                    <div class="text-muted-foreground">Affected: Finance Sector</div>
                  </div>
                </div>
                <div class="font-semibold ml-auto">4h ago</div>
              </div>
              <div class="flex items-center">
                <div class="flex items-center gap-2">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="w-5 h-5 text-green-500"
                  >
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="12" x2="12" y1="8" y2="12"></line>
                    <line x1="12" x2="12.01" y1="16" y2="16"></line>
                  </svg>
                  <div>
                    <div class="font-medium">DDoS Attack Mitigated</div>
                    <div class="text-muted-foreground">Affected: Critical Infrastructure</div>
                  </div>
                </div>
                <div class="font-semibold ml-auto">8h ago</div>
              </div>
              <div class="flex items-center">
                <div class="flex items-center gap-2">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="w-5 h-5 text-blue-500"
                  >
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="12" x2="12" y1="8" y2="12"></line>
                    <line x1="12" x2="12.01" y1="16" y2="16"></line>
                  </svg>
                  <div>
                    <div class="font-medium">Data Breach Detected</div>
                    <div class="text-muted-foreground">Affected: Healthcare Sector</div>
                  </div>
                </div>
                <div class="font-semibold ml-auto">12h ago</div>
              </div>
            </div>
            <div class="flex items-center p-6 pt-0 pb-4 px-6 justify-center bg-gradient-to-b from-background/50 to-background absolute inset-x-0 bottom-0">
              <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 [&amp;_svg]:pointer-events-none [&amp;_svg]:size-4 [&amp;_svg]:shrink-0 border border-input hover:bg-accent hover:text-accent-foreground h-9 px-3 gap-2 rounded-full bg-background">
                View All
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="w-4 h-4"
                >
                  <polyline points="15 3 21 3 21 9"></polyline>
                  <polyline points="9 21 3 21 3 15"></polyline>
                  <line x1="21" x2="14" y1="3" y2="10"></line>
                  <line x1="3" x2="10" y1="21" y2="14"></line>
                </svg>
              </button>
            </div>
          </div>
          <!-- Alerts Card -->
          <div class="rounded-lg border bg-card text-card-foreground shadow-sm relative overflow-hidden" data-v0-t="card">
            <div class="space-y-1.5 p-6 flex flex-row items-center border-b">
              <h3 class="text-2xl font-semibold leading-none tracking-tight">Alerts</h3>
              <p class="text-sm text-muted-foreground ml-auto">
                <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 [&amp;_svg]:pointer-events-none [&amp;_svg]:size-4 [&amp;_svg]:shrink-0 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-9 rounded-md px-3 gap-2">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="w-4 h-4"
                  >
                    <path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"></path>
                    <path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"></path>
                  </svg>
                  Manage
                </button>
              </p>
            </div>
            <div class="grid gap-4 text-sm p-6">
              <div class="flex items-center">
                <div class="flex items-center gap-2">
                  <span class="relative flex shrink-0 overflow-hidden rounded-full w-8 h-8 border">
                    <span class="flex h-full w-full items-center justify-center rounded-full bg-muted">JD</span>
                  </span>
                  <div>
                    <div class="font-medium">John Doe</div>
                    <div class="text-muted-foreground">Ransomware attack detected in the government sector.</div>
                  </div>
                </div>
                <div class="font-semibold ml-auto">2h ago</div>
              </div>
              <div class="flex items-center">
                <div class="flex items-center gap-2">
                  <span class="relative flex shrink-0 overflow-hidden rounded-full w-8 h-8 border">
                    <span class="flex h-full w-full items-center justify-center rounded-full bg-muted">SM</span>
                  </span>
                  <div>
                    <div class="font-medium">Sarah Miller</div>
                    <div class="text-muted-foreground">Phishing campaign targeting the finance sector.</div>
                  </div>
                </div>
                <div class="font-semibold ml-auto">4h ago</div>
              </div>
              <div class="flex items-center">
                <div class="flex items-center gap-2">
                  <span class="relative flex shrink-0 overflow-hidden rounded-full w-8 h-8 border">
                    <span class="flex h-full w-full items-center justify-center rounded-full bg-muted">MK</span>
                  </span>
                  <div>
                    <div class="font-medium">Michael Kumar</div>
                    <div class="text-muted-foreground">DDoS attack on critical infrastructure mitigated.</div>
                  </div>
                </div>
                <div class="font-semibold ml-auto">8h ago</div>
              </div>
              <div class="flex items-center">
                <div class="flex items-center gap-2">
                  <span class="relative flex shrink-0 overflow-hidden rounded-full w-8 h-8 border">
                    <span class="flex h-full w-full items-center justify-center rounded-full bg-muted">LR</span>
                  </span>
                  <div>
                    <div class="font-medium">Lisa Rao</div>
                    <div class="text-muted-foreground">Data breach detected in the healthcare sector.</div>
                  </div>
                </div>
                <div class="font-semibold ml-auto">12h ago</div>
              </div>
            </div>
            <div class="flex items-center p-6 pt-0 pb-4 px-6 justify-center bg-gradient-to-b from-background/50 to-background absolute inset-x-0 bottom-0">
              <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 [&amp;_svg]:pointer-events-none [&amp;_svg]:size-4 [&amp;_svg]:shrink-0 border border-input hover:bg-accent hover:text-accent-foreground h-9 px-3 gap-2 rounded-full bg-background">
                View All
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="w-4 h-4"
                >
                  <polyline points="15 3 21 3 21 9"></polyline>
                  <polyline points="9 21 3 21 3 15"></polyline>
                  <line x1="21" x2="14" y1="3" y2="10"></line>
                  <line x1="3" x2="10" y1="21" y2="14"></line>
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<style scoped>
:root {
  --background: 210 100% 6%;
  --foreground: 180 100% 90%;
  --primary: 200 100% 28%;
  --primary-foreground: 180 100% 90%;
  --secondary: 203 23% 30%;
  --secondary-foreground: 180 100% 90%;
  --accent: 198 70% 50%;
  --accent-foreground: 185 10% 13%;
  --destructive: 0 98% 44%;
  --destructive-foreground: 0 0% 100%;
  --muted: 200 50% 30%;
  --muted-foreground: 180 100% 90%;
  --card: 210 100% 12%;
  --card-foreground: 180 100% 90%;
  --popover: 210 100% 15%;
  --popover-foreground: 180 100% 90%;
  --border: 210 50% 40%;
  --input: 210 50% 40%;
  --ring: 180 100% 90%;
  --chart-1: 200 100% 28%;
  --chart-2: 201 99% 25%;
  --chart-3: 203 98% 22%;
  --chart-4: 204 100% 18%;
  --chart-5: 206 100% 15%;
  --radius: 0rem;
}

h1, h2, h3, h4, h5, h6 {
  font-family: 'Bricolage Grotesque', sans-serif;
  --font-sans-serif: 'Bricolage Grotesque';
}

body {
  font-family: 'Space Mono', monospace;
  --font-monospace: 'Space Mono';
}
</style>

<script>
export default {
  name: 'CyberIncidentMonitor',
};
</script>