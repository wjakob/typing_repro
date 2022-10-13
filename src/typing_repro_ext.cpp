#include <nanobind/nanobind.h>

namespace nb = nanobind;

using namespace nb::literals;

NB_MODULE(typing_repro_ext, m) {

    struct A { };

    nb::class_<A>(m, "A")
        .def(nb::init<>())
        .def("add", [](int a, int b) { return a + b; }, "a"_a, "b"_a);
}
