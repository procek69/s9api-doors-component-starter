# Pierwsza instalacja

## Instalacja narzędzi
```bash
sudo pip3 install virtualenv
```

## Przygotowanie środowiska
```bash
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Uruchomienie serwera
```bash
cd src
./run.sh
```

## Uruchomienie testów
W osobnej konsoli:
```bash
cd test
python3 test.py
```

# Każde kolejne uruchomienie
```bash
source venv/bin/activate
cd src
./run.sh
```

# Przygotowanie na produkcję (Docker)
```bash
./build.sh
```