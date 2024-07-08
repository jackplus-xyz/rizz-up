<script lang="ts">
  import GuidanceLeft2ShortArrow from "~icons/guidance/left-2-short-arrow";
  import GuidanceDown2ShortArrow from "~icons/guidance/down-2-short-arrow";
  import Hero from "$lib/components/Hero.svelte";
  import ImageUpload from "$lib/components/ImageUpload.svelte";
</script>

<svelte:head>
  <title>Rizz Up</title>
  <meta
    name="description"
    content="Rizz Up, a web application that analyzes user skin tones and generates personalized color palettes."
  />
</svelte:head>

<div class="flex w-full flex-col items-center justify-start md:min-h-screen">
  <Hero />
  <div
    class="flex flex-col items-center justify-center px-8 text-lg md:flex-row"
  >
    <div
      class="group flex flex-col items-center justify-center text-lg font-light md:flex-row md:text-2xl"
    >
      Upload a photo to start the analysis
      <span
        class="mx-2 hidden transition-all group-hover:translate-x-2 md:mx-4 md:flex"
        id="upload-arrow"
      >
        <GuidanceLeft2ShortArrow />
      </span>
      <span class="my-4 md:hidden" id="upload-arrow">
        <GuidanceDown2ShortArrow />
      </span>
    </div>
    <ImageUpload />
  </div>
</div>
