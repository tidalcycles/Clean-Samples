# Clean-Samples

Like Dirt-Samples, but cleaned up, with clear provenance and license
info (generally a permissive creative commons licence but check the
metadata for specifics).

The [bin/meta.py](bin/meta.py) python script is a reference
implementation that can make a '.cleanmeta' metadata file for your own
sample pack folder. See below for how to use it and contribute a
sample pack of your own.

If you want to use these outside the Tidal/SuperDirt/SuperCollider
ecosystem you are very welcome. You're encouraged to join discussion
in the github issue tracker so that we can develop a standard way to
share and index/signpost these packs.

See
[/tidalcycles/sounds-repetition](https://github.com/tidalcycles/sounds-repetition)
for an example sample pack which has two sets of samples in it.

## How to contribute a sample pack

Please only contribute samples if you are happy to share them under a
permissive license such as
[CC0](https://creativecommons.org/share-your-work/public-domain/cc0/) or 
a similar [creative commons license](https://creativecommons.org/choose/).

If you are unfamiliar with the 'git' software, please [create an issue
here](https://github.com/tidalcycles/Clean-Samples/issues), with a
short description of your samples and a link to them and someone
should be along to help shortly.

If you are familiar with git and running python scripts (or happy to
learn), please follow the below instructions. This is all new - if
anything is unclear please create an issue, thanks!

1. Get your samples together in .wav format, editing them if necessary (see below for advice).
2. [Create a new repository](https://github.com/new). This isn't
   essential, but consider putting 'sounds-' in front of its name,
   e.g. 'sounds-303bass' for your 303 bass samples.
3. Add your samples to the repository. For an example of how to
   organise them, see this sample pack:
   [tidalcycles/sounds-repetition](https://github.com/tidalcycles/sounsd-repetition),
   which has two sets of samples, with a subfolder for each.
4. Create a '.cleanmeta' metadata file for each subfolder. Again, see
   [tidalcycles/sounds-repetition](https://github.com/tidalcycles/sounds-repetition)
   for examples. There is a python script [bin/meta.py](bin/meta.py)
   which can generate the metadata file for you, run it without
   parameters for help. Here is an example commandline, that was used to generate [repetition.cleanmeta](https://github.com/tidalcycles/sounds-repetition/blob/main/repetition.cleanmeta):

   ```
   ../Clean-Samples/bin/meta.py --sample-subfolder repetition/ --maintainer alex --email alex@slab.org --copyright "(c) 2021 Alex McLean" --license CC0 --provenance "Various dodgy speech synths" --shortname repetition --sample-subfolder repetition --write .
   ```
   After generating the file, edit it with a text editor to fill in any missing info.
5. When ready, add te URL of your repository to the [https://github.com/tidalcycles/Clean-Samples/blob/main/Clean-Samples.quark](dependencies) for the Clean-Samples quark) in a pull request. You could also add it to the [SuperCollider quarks database](https://github.com/supercollider-quarks/quarks/blob/master/directory.txt), or we can do that for you if you prefer, so that we can accept the PR to Clean-Samples once it's accepted as a quark.

## Advice for preparing samples

You can use free/open source software like
[ardour](https://www.audacityteam.org/download/) for editing samples.

As a minimum, be sure to trim any silence from beginning/end of the
samples, and that the start and end of the sample is at zero to avoid
clicks (you might need to fade in / fade out by a tiny amount to
achieve this).

Consider adjusting the volume/loudness too, for example normalising to
-1.0db - but this is very subjective and will depend on the nature of
the samples and the music they're used with. For example distorted
gabba samples are intended to be very loud, and a whisper is intended
to sound silent. The average non-percussive sample should be around
-23dB RMS. Samples shouldn't exceed 0dB true peak. [EBU recommends
-1dBTP at
4x-oversampling](https://tech.ebu.ch/docs/tech/tech3343-v2.pdf).
Samples generally shouldn't have DC offset, although e.g. some kick drum samples
naturally have non-zero mean.

For more advice, you could [join the discussion here](https://github.com/tidalcycles/Clean-Samples/issues/8).

Thanks!
