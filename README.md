# Clean-Samples

Like Dirt-Samples, but cleaned up, with clear provenance and license
(generally CC0 but check the metadata for specifics).

The [bin/meta.py](bin/meta.py) python script is a reference
implementation that can make a '.cleanmeta' metadata file for your own
sample pack folder. See below for how to use it and contribute a
sample pack of yuor own.

If you want to use these outside the supercollider quark ecosystem you
are very welcome. You're encouraged to discuss this in the github
issue tracker so that we can develop a standard way to share and
index/signpost these packs.

See
[/tidalcycles/Clean-reptition](https://github.com/tidalcycles/Clean-repetition)
for an example sample pack which has two sample sets in it.

## How to contribute a sample pack

Please only contribute samples if you are happy to share them under a
permissive license such as
[CC0](https://creativecommons.org/share-your-work/public-domain/cc0/).

If you are unfamiliar with the 'git' software, please [create an issue
here](https://github.com/tidalcycles/Clean-Samples/issues), with a
short description of your samples and if possible a link to them and
someone will be along to help shortly.

If you are familiar with git and running python scripts (or happy to
learn), please follow the below instructions. This is all new - if
anything is unclear please create an issue, thanks!

1. Get your samples together in .wav format. We recommend normalising
   them to xxx dB. Be sure to trim any silence from beginning/end of the
   samples, and that the start/end of the sample is at zero to avoid
   clicks (you might need to fade in / fade out by a tiny amount to
   achieve this).
2. [Create a new repository](https://github.com/new). If your sample
   pack is called '303bass', put 'Clean-' in front, e.g. 'Clean-303bass'.
3. Add your samples to the repository. For an example of how to
   organise them, see this sample pack:
   [tidalcycles/Clean-repetition](https://github.com/tidalcycles/Clean-repetition),
   which has two sets of samples, with a subfolder for each.
4. Create a '.cleanmeta' metadata file for each subfolder. Again, see
   [tidalcycles/Clean-repetition](https://github.com/tidalcycles/Clean-repetition)
   for examples. There is a python script [bin/meta.py](bin/meta.py)
   which can generate the metadata file for you, run it without
   parameters for help. Here is an example commandline, that was used to generate [repetition.cleanmeta](https://github.com/tidalcycles/Clean-repetition/blob/main/repetition.cleanmeta):

   ```
   ../Clean-Samples/bin/meta.py --sample-subfolder repetition/ --maintainer alex --email alex@slab.org --copyright "(c) 2021 Alex McLean" --license CC0 --provenance "Various dodgy speech synths" --shortname repetition --sample-subfolder repetition --write .
   ```
   After generating the file, edit it with a text editor to fill in any missing info.

