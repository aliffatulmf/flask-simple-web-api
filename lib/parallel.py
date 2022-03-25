from multiprocessing import Process, Manager


def multiprocess(iter, value, ns):
    if iter["id"] == value:
        ns.append(iter)


def parallel_search(iter: list, value: int):
    manager = Manager()
    ns = manager.list()
    jobs = []

    for i in iter:
        p = Process(target=multiprocess, args=(i, value, ns))
        jobs.append(p)

    for j in jobs:
        j.run()

    return ns
