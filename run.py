#!/usr/bin/env python3
"""
Script simples para executar o cliente React e o servidor Flask simultaneamente usando threading.
"""

from pathlib import Path
import subprocess
import threading
import time

class Main:
    def __init__(self):
        # Criar threads para executar servidor e cliente
        server_thread = threading.Thread(target=self.run_server, daemon=True)
        client_thread = threading.Thread(target=self.run_client, daemon=True)

        # Iniciar threads
        server_thread.start()
        time.sleep(2)  # Aguardar servidor inicializar
        client_thread.start()

        try:
            # Manter o programa principal rodando
            while True:
                if not server_thread.is_alive() or not client_thread.is_alive():
                    print("⚠️  Um dos processos foi encerrado.")
                    break
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Encerrando aplicação...")

        print("✅ Aplicação encerrada.")
        
    def run_server(self):
        """Executa o servidor Flask."""
        server_dir = Path(__file__).parent / "server"
        python_path = server_dir / "env" / "bin" / "python"

        print("🚀 Iniciando servidor Flask na porta 8080...")
        try:
            subprocess.run([str(python_path), "main.py"], cwd=server_dir, check=True)
        except KeyboardInterrupt:
            print("🛑 Servidor Flask encerrado.")
        except Exception as e:
            print(f"❌ Erro no servidor Flask: {e}")

    def run_client(self):
        """Executa o cliente React."""
        client_dir = Path(__file__).parent / "client"

        print("🚀 Iniciando cliente React...")
        try:
            subprocess.run(["npm", "run", "dev"], cwd=client_dir, check=True)
        except KeyboardInterrupt:
            print("🛑 Cliente React encerrado.")
        except Exception as e:
            print(f"❌ Erro no cliente React: {e}")


if __name__ == "__main__":
    Main()
