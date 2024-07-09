<script lang="ts">
  import ArrowLink from "$lib/components/ArrowLink.svelte";

  function clearLocalStorage() {
    const theme = localStorage.getItem("theme");
    localStorage.clear();
    if (theme) {
      localStorage.setItem("theme", theme);
    }
  }
</script>

<svelte:head>
  <title>Rizz Up</title>
  <meta
    name="description"
    content="Rizz Up, a web application that analyzes user skin tones and generates personalized color palettes."
  />
</svelte:head>

<div
  class="mx-auto flex min-h-[80vh] w-3/4 flex-col items-center justify-center font-serif md:min-h-screen"
>
  <h1>Oopsy!</h1>
  <p>
    Looks like something isn't working. Keep calm and give it another try or
    come back later.
  </p>
  <button
    on:click={clearLocalStorage}
    class="mt-8 font-sans text-xl font-extralight"
  >
    <ArrowLink text="Go back to home" link="/" />
  </button>
</div>
