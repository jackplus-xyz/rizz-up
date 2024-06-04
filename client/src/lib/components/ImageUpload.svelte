<script lang="ts">
	import { FileDropzone } from '@skeletonlabs/skeleton';
	import MdiLightCloudUpload from '~icons/mdi-light/cloud-upload';
	import SvgSpinners3DotsMove from '~icons/svg-spinners/3-dots-move';
	import { Button } from '$lib/components/ui/button';
	import { goto } from '$app/navigation';
	import { fade } from 'svelte/transition';
	import { serverUrl } from '$lib/config.js';
	import { imgSrc as imgSrcStore } from '$lib/stores';

	let files: FileList;
	let errorMessage = '';
	let imgSrc = '';
	$: showImage = imgSrc !== '';
	let skinTone = '';
	let isError = false;
	let isUploading = false;

	function onChangeHandler(e: Event): void {
		const target = e.target as HTMLInputElement;
		if (target.files && target.files.length > 0) {
			const file = target.files[0];
			const reader = new FileReader();
			reader.onload = () => {
				imgSrc = reader.result as string;
			};
			reader.readAsDataURL(file);
		}
	}

	function clearImage(): void {
		isError = false;
		imgSrc = '';
	}

	async function submitImage(): Promise<void> {
		if (!files) {
			handleError('No image to submit');
			return;
		}

		try {
			isError = false;
			isUploading = true;
			const formData = new FormData();
			formData.append('image', files[0]);

			const response = await fetch(`${serverUrl}/image`, {
				method: 'POST',
				body: formData
			});

			if (!response.ok) {
				const errorData = await response.json();
				console.error(errorData.error);
				handleError(errorData.error);
				return;
			}

			const data = await response.json();
			if (data.skin_tone) {
				skinTone = data.skin_tone;
				const facial_area = data.facial_area;

				const croppedImageSrc = await cropImage(imgSrc, facial_area, 200);
				imgSrcStore.set(croppedImageSrc);

				const formattedSkinTone = skinTone.replace('#', '');
				goto(`/analysis/${formattedSkinTone}`);
			}
		} catch (error) {
			handleError('Failed to process the image. Please try another photo or try again later.');
		} finally {
			isUploading = false;
		}

		function cropImage(
			src: string,
			cropArea: [number, number, number, number],
			padding: number = 0
		): Promise<string> {
			const [x, y, x2, y2] = cropArea;
			const width = x2 - x;
			const height = y2 - y;

			// Calculate the size of the square crop with padding
			const size = Math.max(width, height) + padding * 2;

			// Calculate the center of the original crop area
			const centerX = x + width / 2;
			const centerY = y + height / 2;

			// Calculate the new top-left corner of the crop area with padding
			const newX = centerX - size / 2;
			const newY = centerY - size / 2;

			const canvas = document.createElement('canvas');
			const ctx = canvas.getContext('2d');

			// Set canvas size to the size of the square crop with padding
			canvas.width = size;
			canvas.height = size;

			// Create an image element
			const image = new Image();
			image.src = src;

			if (!ctx) {
				console.error('Unable to get 2D rendering context');
				return Promise.reject('Unable to get 2D rendering context');
			}

			// Ensure the image is loaded before drawing it onto the canvas
			return new Promise((resolve, reject) => {
				image.onload = () => {
					// Draw the image onto the canvas, centering it and applying padding
					ctx.drawImage(image, newX, newY, size, size, 0, 0, size, size);

					// Convert the canvas to a data URL and return it
					resolve(canvas.toDataURL());
				};

				image.onerror = reject;
			});
		}
	}

	function handleError(message: string): void {
		isError = true;
		errorMessage = message;
	}
</script>

{#if showImage}
	<div
		class="flex h-fit max-w-sm flex-col items-center justify-center rounded-xl border bg-primary-foreground p-4"
	>
		<img
			src={imgSrc}
			alt="Preview"
			class="w-full rounded-lg transition-opacity duration-300"
			class:opacity-50={isUploading}
			in:fade
		/>
		<div class="mt-4 flex items-center space-x-4" in:fade>
			<Button on:click={submitImage} disabled={isUploading}>Submit</Button>
			<Button on:click={clearImage} variant="outline" disabled={isUploading}>Clear</Button>
		</div>
		{#if isError || isUploading}
			<div
				class="mt-4 text-sm"
				class:text-destructive={isError}
				class:text-muted-foreground={isUploading}
				in:fade
			>
				{#if isError}
					{errorMessage}
				{:else}
					<SvgSpinners3DotsMove />
				{/if}
			</div>
		{/if}
	</div>
{:else}
	<div
		role="none"
		id="upload-image"
		class=" flex aspect-square max-w-md flex-col items-center justify-center rounded-xl border bg-primary-foreground text-base text-muted-foreground transition duration-200 hover:bg-background"
	>
		<MdiLightCloudUpload class="text-4xl" />
		<FileDropzone
			name="files"
			class="border-none"
			type="file"
			bind:files
			on:change={onChangeHandler}
		>
			<svelte:fragment slot="message">
				Click to upload a photo or drag and drop it here.
			</svelte:fragment>
			<svelte:fragment slot="meta">Allowed formats: PNG and JPG.</svelte:fragment>
		</FileDropzone>
	</div>
{/if}
