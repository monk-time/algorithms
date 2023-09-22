from dataclasses import dataclass


@dataclass
class Person:
    pos: int
    rating: int
    programs: list[int]


def enroll(program_spots: list[int], priorities: list[list[int]]) -> list[int]:
    persons = [
        Person(pos=index, rating=rating, programs=programs)
        for index, (rating, _, *programs) in enumerate(priorities)
    ]
    persons.sort(key=lambda person: person.rating)
    program_spots = [0] + program_spots  # programs are counted from 1
    admissions = [-1] * len(persons)
    for person in persons:
        for program in person.programs:
            if program_spots[program]:
                program_spots[program] -= 1
                admissions[person.pos] = program
                break
    return admissions


if __name__ == '__main__':
    person_count, program_count = [int(s) for s in input().split()]
    program_spots = [int(s) for s in input().split()]
    priorities = [
        [int(s) for s in input().split()] for _ in range(person_count)
    ]
    print(*enroll(program_spots, priorities))
