from setuptools import setup, find_packages

requirements = [
    "tqdm",
    "kaldiio",
    "torch>=1.12.0",
    "torchaudio>=0.12.0",
    "silero-vad @ git+https://github.com/pengzhendong/silero-vad.git@e26af177ed379e1cb9931e6f0299ea0f89206c6a",
]

setup(
    name="wespeaker",
    install_requires=requirements,
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "wespeaker = wespeaker.cli.speaker:main",
        ]
    },
)
