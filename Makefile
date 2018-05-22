srpm: kitty.spec
	fedpkg --release f28 srpm
	copr-cli build gagbo/kitty-latest kitty-0.8.2-1.fc28.src.rpm

