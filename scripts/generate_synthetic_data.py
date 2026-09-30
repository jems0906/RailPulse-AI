import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from training.data_loader import save_samples

if __name__ == "__main__":
    save_samples()
    print("Synthetic shipment data written to data_samples/shipments.csv")
