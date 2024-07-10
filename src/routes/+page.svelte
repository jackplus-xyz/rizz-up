<script lang="ts">
  import GuidanceLeft2ShortArrow from "~icons/guidance/left-2-short-arrow";
  import GuidanceDown2ShortArrow from "~icons/guidance/down-2-short-arrow";
  import Hero from "$lib/components/Hero.svelte";
  import ImageUpload from "$lib/components/ImageUpload.svelte";

  const tip = {
    title: "Tip",
    description:
      "Use a photo with natural lighting, minimal shadows, and no filters for the most accurate analysis.",
  };
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
    class="mb-8 flex flex-col items-center justify-center px-8 text-lg md:mb-16 md:flex-row"
  >
    <div
      class="group flex flex-col items-center justify-center text-lg font-light md:flex-row md:text-2xl"
    >
      <div
        class="flex max-w-xs flex-col items-start justify-center md:max-w-sm"
      >
        <div class="whitespace-nowrap">
          Upload a photo to start the analysis
        </div>
        <div class="mt-4 text-sm text-muted-foreground">
          {tip.title}: {tip.description}
        </div>
      </div>
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
