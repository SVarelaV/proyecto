class DatoClinico:
    def __init__(
            self, idDatoClinico, dni, fechaRegistro,
            antecedentesAlzheimer, enfermedadesPrevias, depresionDiagnoticada,
            accidenteCerebroVascular, trastornoSueno, medicacionActual,
            fumador, alchol, actividadFisica, alimentacionSaludable,
            horasSueno, calidadSueno, nivelesEstres
    ):

        self.idDatoClinico = idDatoClinico
        self.dni = dni
        self.fechaRegistro = fechaRegistro
        self.antecedentesAlzheimer = antecedentesAlzheimer
        self.enfermedadesPrevias = enfermedadesPrevias
        self.depresionDiagnoticada = depresionDiagnoticada
        self.accidenteCerebroVascular = accidenteCerebroVascular
        self.trastornoSueno = trastornoSueno
        self.medicacionActual = medicacionActual
        self.fumador = fumador
        self.alchol = alchol
        self.actividadFisica = actividadFisica
        self.alimentacionSaludable = alimentacionSaludable
        self.horasSueno = horasSueno
        self.calidadSueno = calidadSueno
        self.nivelesEstres = nivelesEstres

    @property
    def idDatoClinico(self):
        return self.idDatoClinico

    @idDatoClinico.setter
    def idDatoClinico(self, idDatoClinico):
        self.idDatoClinico = idDatoClinico

    @property
    def dni(self):
        return self.dni

    @dni.setter
    def dni(self, dni):
        self.dni = dni

    @property
    def fechaRegistro(self):
        return self.fechaRegistro

    @fechaRegistro.setter
    def fechaRegistro(self, fechaRegistro):
        self.fechaRegistro = fechaRegistro

    @property
    def antecedentesAlzheimer(self):
        return self.antecedentesAlzheimer

    @antecedentesAlzheimer.setter
    def antecedentesAlzheimer(self, antecedentesAlzheimer):
        self.antecedentesAlzheimer = antecedentesAlzheimer

    @property
    def enfermedadesPrevias(self):
        return self.enfermedadesPrevias

    @enfermedadesPrevias.setter
    def enfermedadesPrevias(self, enfermedadesPrevias):
        self.enfermedadesPrevias = enfermedadesPrevias

    @property
    def depresionDiagnoticada(self):
        return self.depresionDiagnoticada

    @depresionDiagnoticada.setter
    def depresionDiagnoticada(self, depresionDiagnoticada):
        self.depresionDiagnoticada = depresionDiagnoticada

    @property
    def accidenteCerebroVascular(self):
        return self.accidenteCerebroVascular

    @accidenteCerebroVascular.setter
    def accidenteCerebroVascular(self, accidenteCerebroVascular):
        self.accidenteCerebroVascular = accidenteCerebroVascular

    @property
    def trastornoSueno(self):
        return self.trastornoSueno

    @trastornoSueno.setter
    def trastornoSueno(self, trastornoSueno):
        self.trastornoSueno = trastornoSueno

    @property
    def medicacionActual(self):
        return self.medicacionActual

    @medicacionActual.setter
    def medicacionActual(self, medicacionActual):
        self.medicacionActual = medicacionActual

    @property
    def fumador(self):
        return self.fumador

    @fumador.setter
    def fumador(self, fumador):
        self.fumador = fumador

    @property
    def alchol(self):
        return self.alchol

    @alchol.setter
    def alchol(self, alchol):
        self.alchol = alchol

    @property
    def actividadFisica(self):
        return self.actividadFisica

    @actividadFisica.setter
    def actividadFisica(self, actividadFisica):
        self.actividadFisica = actividadFisica

    @property
    def alimentacionSaludable(self):
        return self.alimentacionSaludable

    @alimentacionSaludable.setter
    def alimentacionSaludable(self, alimentacionSaludable):
        self.alimentacionSaludable = alimentacionSaludable

    @property
    def horasSueno(self):
        return self.horasSueno

    @horasSueno.setter
    def horasSueno(self, horasSueno):
        self.horasSueno = horasSueno

    @property
    def calidadSueno(self):
        return self.calidadSueno

    @calidadSueno.setter
    def calidadSueno(self, calidadSueno):
        self.calidadSueno = calidadSueno

    @property
    def nivelesEstres(self):
        return self.nivelesEstres

    @nivelesEstres.setter
    def nivelesEstres(self, nivelesEstres):
        self.nivelesEstres = nivelesEstres
