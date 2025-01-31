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