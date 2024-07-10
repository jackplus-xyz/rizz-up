<script>
  import { quadInOut } from "svelte/easing";
  import { fly } from "svelte/transition";
  import GuidanceLeft2ShortArrow from "~icons/guidance/left-2-short-arrow";
</script>

<svelte:head>
  <title>Rizz Up | Contact</title>
  <meta name="description" content="Contact Rizz Up" />
</svelte:head>

<div
  class="mx-auto flex min-h-screen flex-col items-start justify-center px-8 py-4 font-serif md:w-3/4 md:px-16 md:py-8 lg:w-1/2"
>
  <h1 in:fly={{ y: 50, duration: 500, easing: quadInOut }}>Contact</h1>

  <p in:fly={{ y: 50, duration: 500, delay: 100, easing: quadInOut }}>
    Thanks for trying Rizz Up! If you have any questions, suggestions, or
    feedback about Rizz Up, you can find me through the following methods:
  </p>

  <div
    class="mt-8"
    in:fly={{ y: 50, duration: 500, delay: 200, easing: quadInOut }}
  >
    <h2 class="mb-4 text-xl font-bold">Contact Information</h2>
    <ul class="ml-6 list-disc space-y-2">
      <li>
        <a
          href="mailto:rizzup@jackplus.xyz"
          class="text-blue-500 hover:underline">Email</a
        >
      </li>
      <li>
        <a
          href="https://jackplus.xyz"
          target="_blank"
          rel="noopener noreferrer"
          class="text-blue-500 hover:underline">Website</a
        >
      </li>
      <li>
        <a
          href="https://twitter.com/jackplus-xyz"
          target="_blank"
          rel="noopener noreferrer"
          class="text-blue-500 hover:underline">Twitter</a
        >
      </li>
      <li>
        <a
          href="https://www.linkedin.com/in/jackplus-xyz"
          target="_blank"
          rel="noopener noreferrer"
          class="text-blue-500 hover:underline">LinkedIn</a
        >
      </li>
    </ul>
  </div>

  <p
    class="mt-8"
    in:fly={{ y: 50, duration: 500, delay: 300, easing: quadInOut }}
  >
    I aim to respond to inquiries as soon as possible. Thank you for your
    interest in Rizz Up!
  </p>

  <div
    class="flex w-full items-center justify-center py-4 md:py-8"
    in:fly={{ y: 50, duration: 500, delay: 400, easing: quadInOut }}
  >
    <h2>
      <a href="/" class="group relative flex">
        Back to Home
        <span class="ml-2 transition-all group-hover:translate-x-2 md:ml-4">
          <GuidanceLeft2ShortArrow />
        </span>
      </a>
    </h2>
  </div>
</div>
