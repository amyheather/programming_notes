# Linux

## Resize an image

imagemagick

convert -resize 20% source.png dest.jpg

## Reinstall google chrome

Install the `.deb` file (as not available in the official APT repositories).

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

Install google chrome.

```
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

Remove the `.deb` file.

```
sudo rm google-chrome-stable_current_amd64.deb
```

## Upgrade quarto

Install the `.deb` file, then run e.g....

```
sudo dpkg -i quarto-1.6.40-linux-amd64.deb
```

## Videos

Trim video length:

```{.bash}
ffmpeg -ss 00:00:01.2 -i vscode.webm -t 00:00:05.5 -c:v libvpx-vp9 -c:a libopus vscode_crop.webm
```

Convert to GIF:

```{.bash}
ffmpeg -ss 00:00:01.2 -i vscode.webm -t 00:00:05.5 -c:v libvpx-vp9 -c:a libopus vscode_crop.webm
```