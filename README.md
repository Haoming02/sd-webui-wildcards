# SD Webui Wildcards
This is an Extension for the [Automatic1111 Webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui), which allows you to use wildcards in your prompts.

**Note:** Since I chose to use **curly brackets** as the syntax, this Extension will be incompatible with many other prompt-assisting Extensions. *(**eg.** [Dynamic Prompts](https://github.com/adieyal/sd-dynamic-prompts))*

## How to Use
When you write the prompts *(works for `positive prompt`, `negative prompt`, and `hires. fix prompts`)*, you can use the syntax `{trigger}` to invoke the wildcards. This Extension will then replace the syntax with a random entry from the specified file.
The **trigger** refers to the **filename** of the wildcard file. Within the file, you can write multiple available tags, each in its own separate line.

> An example file `color.txt` is provided

> **Tip:** You can use ChatGPT to generate a list of tags for you

<hr>

<sup> Yes, I rewrote this Extension solely because I want to use `{trigger}` instead of `__trigger__` </sup>
