<script lang="ts">
  import { page } from "$app/stores";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu";
  import ThemeToggle from "$lib/components/ThemeToggle.svelte";
  import HealthiconsUiMenuOutline from "~icons/healthicons/ui-menu-outline";

  const routes = [
    {
      name: "About",
      path: "/about",
    },
    {
      name: "Contact",
      path: "/contact",
    },
    {
      name: "Support",
      path: "/support",
    },
  ];

  function isActive(path: string): boolean {
    return Boolean(
      $page.url.pathname === path || $page.url.pathname.startsWith(path),
    );
  }

  // Metadata
  const title = "Rizz Up";
  const description =
    "Discover the perfect colors that complement your skin tone and style.";
  const image = `${$page.url.origin}/logo.png`;
  const url = "https://rizz-up.jackplus.xyz";
  const siteName = "Rizz Up";
</script>

<svelte:head>
  <title>{title}</title>
  <meta name="description" content={description} />

  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png" />
  <link rel="manifest" href="/site.webmanifest" />

  <!-- OpenGraph tags -->
  <meta property="og:title" content={title} />
  <meta property="og:description" content={description} />
  <meta property="og:image" content={image} />
  <meta property="og:url" content={url} />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content={siteName} />

  <!-- Twitter Card tags -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content={title} />
  <meta name="twitter:description" content={description} />
  <meta name="twitter:image" content={image} />
</svelte:head>

<header class="flex items-center justify-between px-6 py-4 md:px-8">
  <a href="/" class="font-serif text-2xl font-bold italic md:hidden">
    <span>Rizz Up</span>
  </a>
  <nav class="hidden items-center justify-center space-x-4 md:flex">
    <a href="/" class="mr-4 font-serif text-2xl font-bold italic">
      <span>Rizz Up</span>
    </a>
    {#each routes as route}
      <div
        aria-current={isActive(route.path) ? "page" : undefined}
        class="font-serif text-lg italic underline-offset-4 transition duration-100 ease-in-out hover:underline"
      >
        <a href={route.path}>{route.name}</a>
      </div>
    {/each}
  </nav>
  <div class="flex h-full space-x-4 md:hidden">
    <ThemeToggle outline={false} />
    <DropdownMenu.Root>
      <DropdownMenu.Trigger>
        <HealthiconsUiMenuOutline />
      </DropdownMenu.Trigger>
      <DropdownMenu.Content>
        <DropdownMenu.Group>
          {#each routes as route}
            <DropdownMenu.Item>
              <a href={route.path}>{route.name}</a>
            </DropdownMenu.Item>
          {/each}
        </DropdownMenu.Group>
      </DropdownMenu.Content>
    </DropdownMenu.Root>
  </div>
  <div class="hidden md:flex">
    <ThemeToggle />
  </div>
</header>
