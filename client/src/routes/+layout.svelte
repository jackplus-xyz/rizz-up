<script>
  import "../app.css";
  import Header from "$lib/components/Header.svelte";
  import Footer from "$lib/components/Footer.svelte";
</script>

<div class="min-h-screen text-primary">
  <Header />
  <main
    class="h-full w-full bg-gradient-to-br from-neutral-50 to-neutral-100 dark:from-neutral-800 dark:to-neutral-900"
  >
    <slot />
  </main>
  <Footer />
</div>
