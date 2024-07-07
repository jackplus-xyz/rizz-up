<script>
  export let title;
  export let description;
</script>

<div
  class="flex h-fit w-full flex-col items-start justify-center rounded-2xl border bg-muted p-4 text-base text-muted-foreground"
>
  <span class="font-bold">
    {title}
  </span>
  <p class="my-2 text-base text-muted-foreground">
    {@html description}
  </p>
</div>
