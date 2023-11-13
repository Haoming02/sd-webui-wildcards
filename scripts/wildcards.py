import random
import sys
import os
import re

from modules import scripts

wildcards_folder = os.path.join(scripts.basedir(), 'wildcards')

class WildcardsScript(scripts.Script):
    def title(self):
        return 'Neo Wildcards'

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def replace_prompts(self, prompt:str, seed:int):
        if len(prompt.strip()) == 0:
            return prompt

        def replace(match):
            key = match.group(1)

            try:
                with open(os.path.join(wildcards_folder, f'{key}.txt'), 'r') as Tags:
                    lines = Tags.read().strip().split('\n')

                l = len(lines)

                random.seed(seed)
                i = random.randint(1, l)

                return lines[i - 1]

            except FileNotFoundError:
                print(f'\n\n[Wildcards] File "{key}" is not Found!\n')
                return ''

        pattern = re.compile(r'\{([^}]+)\}')
        result = pattern.sub(replace, prompt)

        return result

    def process(self, p):
        batch_size = len(p.all_prompts)

        for i in range(batch_size):
            p.all_prompts[i] = self.replace_prompts(p.all_prompts[i], p.all_seeds[i])
            p.all_negative_prompts[i] = self.replace_prompts(p.all_negative_prompts[i], p.all_seeds[i])

            if hasattr(p, 'all_hr_prompts') and p.all_hr_prompts is not None and len(p.all_hr_prompts) > 0:
                p.all_hr_prompts[i] = self.replace_prompts(p.all_hr_prompts[i], p.all_seeds[i])
            if hasattr(p, 'all_hr_negative_prompts') and p.all_hr_negative_prompts is not None and len(p.all_hr_negative_prompts) > 0:
                p.all_hr_negative_prompts[i] = self.replace_prompts(p.all_hr_negative_prompts[i], p.all_seeds[i])

        return p
