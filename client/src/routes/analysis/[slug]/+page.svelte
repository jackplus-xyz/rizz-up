<script lang="ts">
  import { fade } from "svelte/transition";
  import { imgSrc } from "$lib/stores";
  import SwatchSlide from "$lib/components/SwatchSlide.svelte";
  import SwatchButton from "$lib/components/SwatchButton.svelte";
  import type { PageData } from "./+page.ts";
  import GuidanceDown2ShortArrow from "~icons/guidance/down-2-short-arrow";
  import SvgSpinners3DotsMove from "~icons/svg-spinners/3-dots-move";

  export let data: PageData;
  const { skinTone, colors, season } = data.analysis;

  let selectedColor = skinTone;

  $: isLoading = !data;

  function handleColorSelected(event: CustomEvent<{ color: string }>) {
    selectedColor = event.detail.color;
  }
</script>

<div
  class="flex min-h-screen w-full flex-col items-center justify-center text-2xl font-light"
>
  {#if isLoading}
    <SvgSpinners3DotsMove class="text-3xl text-muted-foreground" />
  {:else}
    <div
      class="mx-auto flex flex-col items-start justify-center px-8 py-8 md:w-3/4 md:py-4 lg:w-1/2"
    >
      <div
        class="flex w-full flex-col items-center justify-start text-lg md:flex-row md:text-2xl"
      >
        {#if $imgSrc !== ""}
          <div
            class="flex h-fit max-w-sm flex-col items-center justify-center rounded-xl border bg-primary-foreground p-4"
          >
            <div class="relative w-full">
              <img
                src={$imgSrc}
                alt="UploadedImage"
                class="w-full rounded-lg"
                in:fade
              />
              <span
                class="absolute bottom-0 left-0 h-1/6 w-full rounded-b-lg transition-colors duration-200 ease-in-out"
                in:fade
                style="background-color: {selectedColor};"
              />
            </div>
          </div>
        {/if}
        <div
          class="mt-4 flex w-full flex-col items-center justify-start space-y-2 md:space-y-4"
        >
          <span> Your skin tone </span>
          <GuidanceDown2ShortArrow />
          <div
            class="aspect-square w-full max-w-[8rem] rounded-xl md:rounded-3xl"
          >
            <SwatchButton
              color={skinTone}
              duration={500}
              on:colorSelected={handleColorSelected}
            />
          </div>
        </div>
      </div>
      <div
        class="my-4 flex flex-col items-center justify-center text-lg md:mt-8 md:text-2xl"
      >
        It is {season} season. These are the colors that compliment your skin tone
        the most
      </div>
      <SwatchSlide {colors} on:colorSelected={handleColorSelected} />
    </div>
  {/if}
  <!-- TODO: Share Button, Save Button -->
</div>
