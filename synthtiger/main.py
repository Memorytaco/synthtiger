"""
SynthTIGER
Copyright (c) 2021-present NAVER Corp.
MIT license
"""

from os import cpu_count
import pprint
import time
from typing import Annotated, Optional

import typer

import synthtiger

main = typer.Typer()

@main.command()
def entry(
script: Annotated[str, typer.Argument(
    help="Script file path."
)],
name: Annotated[str, typer.Option(
    help="Template class name."
)],
config: Annotated[str, typer.Option(
    help="Config file path."
)],
output: Annotated[str, typer.Option(
    help="Directory path to save data."
)],
worker: Annotated[int, typer.Option(
    help="Number of workers. If 0, It generates data in the main process."
)] = cpu_count() or 0,
seed: Annotated[Optional[int], typer.Option(
    help="Random seed."
)] = None,
count: Annotated[int, typer.Option(
    help="Number of output data."
)] = 100,
verbose: Annotated[bool, typer.Option(
    help="Print error messages while generating data."
)] = False
):
    start_time = time.time()

    config = synthtiger.read_config(config)
    pprint.pprint(config)
    synthtiger.set_global_random_seed(seed)
    template = synthtiger.read_template(script, name, config)
    generator = synthtiger.generator(
        script,
        name,
        config=config,
        count=count,
        worker=worker,
        seed=seed,
        retry=True,
        verbose=verbose,
    )

    template.init_save(output)

    for idx, (task_idx, data) in enumerate(generator):
        template.save(output, data, task_idx)
        print(f"Generated {idx + 1} data (task {task_idx})")

    template.end_save(output)

    end_time = time.time()
    print(f"{end_time - start_time:.2f} seconds elapsed")

if __name__ == "__main__":
    main()
