import os
import math

from compas.geometry import scale_vector
from compas.geometry import Vector
from compas.geometry import Rotation
from compas.geometry import Translation
from compas.geometry import Scale
from compas.datastructures import Mesh
from compas_cgal.meshing import mesh_remesh

from compas_cgal import HERE


def test_remeshing():
    FILE = os.path.join(HERE, "..", "data", "Bunny.ply")

    # ==============================================================================
    # Get the bunny and construct a mesh
    # ==============================================================================

    bunny = Mesh.from_ply(FILE)

    bunny.remove_unused_vertices()

    # ==============================================================================
    # Move the bunny to the origin and rotate it upright.
    # ==============================================================================

    vector = scale_vector(bunny.centroid, -1)

    T = Translation.from_vector(vector)
    S = Scale.from_factors([100, 100, 100])
    R = Rotation.from_axis_and_angle(Vector(1, 0, 0), math.radians(90))

    bunny.transform(R * S * T)

    # ==============================================================================
    # Remesh
    # ==============================================================================

    V, F = mesh_remesh(bunny, 1)

    mesh = Mesh.from_vertices_and_faces(V, F)
    print(mesh)
