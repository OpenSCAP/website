A new texts for OpenSCAP portal.

# Features

## Security Compliance
+ What is it?
+ Why it gets done?
+ How to get started?

Security compliance is a state of computer infrastructure that is in line of a security
policy. In ever changing world the infrastructure is never compliant with the policy
in full. Thus, security compliance has evolved to a continuous process that includes
adjustments to the security policy, periodic assessment, and risk monitoring. OpenSCAP
ecosystem provides tools and vanilla policies for quick, cost effective and flexible
implementation of such process.

Security compliance focuses mainly on proper software configuration and software inventory
whereas _Vulnerability Assessment_ inspects installed software for unpatched
vulnerabilities. With OpenSCAP organizations can implement both approaches with the same
tooling, reducing management overhead.

Linux deployments are thriving beyond any point in history. This is the most evident in
cloud infrastructures that are highly dependent on open source software and Linux
operating system is in the basic building block for inexpensive cloud. OpenSCAP was
designed to perform the best in Linux environments and security specialists teamed
together around OpenSCAP to write _security policies_ and hardening guidances for Linux
systems and common server applications.

## Vulnerability Assessment
+ What is it?
+ How to get started?
+ What is a zerodate?
+ How to get OVAL definitions from vendors?
+ How OpenSCAP helps?
  + And what about containers

Vulnerability Assessment is a process that identifies and classifies vulnerabilities
on a system. There is nothing more embarrassing for a security technician when their
systems are compromised by exploiting vulnerability that has been known for months.
Therefore a timely inspection of software inventory is a must for todays organizations.
OpenSCAP ecosystem provides tools for automated vulnerability checking.

Vulnerability Assessment focuses mainly on known security defects in the installed
software whereas _Security Compliance_ asserts for correct software configuration.

The search for security defects is aided by an enumeration of publicly known
vulnerabilities. The MITRE Corporation collaborates with software vendors and they
maintain a list of publicly known vulnerabilities in software products. The naming
scheme is called _CVE_ (Common Vulnerability and Exposures) and it has become widely
known and it is accepted by a community of software vendors.

## For Businesses
+ Protecting business
+ PCI-DSS
+ Testimonials

## For Governments
+ OpenSCAP implements mandatory requirements
+ OpenSCAP is certified

## Open source
+ OpenSCAP ecosystem is 100% open source.
+ What does it mean for users?

## Standards
+ Which standards?
+ Why using standards?
+ General intro into standards ecosystem, fisma act, nist, mitre
+ OpenSCAP is certified

### SCAP Standard
SCAP, pronounced “S-CAP”, is a synthesis of interoperable specifications that
standardize the format and nomenclature by which software flaw and security
configuration information is communicated, both to machines and humans. SCAP
is a multi-purpose framework of specifications that supports automated configuration,
vulnerability and patch checking, technical control compliance activities, and
security measurement.

In other words, SCAP is vendor neutral way of expressing security policy. As such
it enjoys significant use in modern enterprises. SCAP specifications allow for
creation of an ecosystem where the format of security content is well known and
standardized while the implementation of scanner or policy editor is not mandated.
Such status enables organizations to build their _Security Policy_ once, no matter
how many security vendors do they employ.

### SCAP components
SCAP standard family comprises of multiple component standard. The components are
designed to work together the common goal. For each component the standard defines
a document format with syntax and semantics of the internal data structures. All
the component standards are based on Extensible Markup Language (XML) and each
component standard defines its own XML namespace. Different versions of the same
component standard (language) may also be distinguished by different XML namespace.

+ XCCDF (*perhaps separate page as defined below*)
+ OVAL
+ DataStream
+ ARF
+ CPE
+ CVE
+ CWE

#### XCCDF
The XCCDF acronym stands for Extensible Configuration Checklist Description Format.
As the name suggests, the language is used to describe the security checklists. The
language is designed to support information interchange, document generation,
organizational and situational tailoring, automated compliance testing, and compliance
scoring.

The language contains no commands to perform the scan and it is mostly descriptive.
Other component documents may be referred from the XCCDF, so one could come to the
conclusion that the XCCDF binds all other component standards together. If the XCCDF
document is written carefully, it is possible to achieve document which is portable
among all the target platforms, and only the assessment documents (OVAL, OCIL) would
differ.

Like all the SCAP languages, the XCCDF is based on XML and defines its XML elements
and attributes. Figure (*insert figure*) represents a simple XML DOM structure of
XCCDF document. The XCCDF documents tend to be several hundred lines long. The
following section describes main XCCDF elements briefly, focusing on the relation
between them. The language specification describes all the elements in greater detail,
and it can be consulted in the _NIST Interagency Report 7275 Revision 4_.

#### SCE page
+ what is SCE?
  + purpose
  + use case
+ then definition:
  + http://www.open-scap.org/page/SCE

### Other standards
+ SACM
+ SWID
+ CC
+ FIPS

### How we contribute
+ OpenSCAP team has several contributions to SCAP standard

## Acronyms
+ AI: Asset Identification, part of SCAP standard, a language to provide a data model
  for identifying assets, methods for identifying assets, and guidance how to use
  asset identification.
+ ARF: Asset Reporting Format, part of SCAP standard, a language to express the
  transport format of information about assets, and the relationships between assets
  and reports.
+ CC: Common Criteria
+ CCE: Common Configuration Enumeration, part of SCAP standard, an enumeration of
  security relevant configuration elements for applications and operation systems.
+ CCSS:
+ CIS
+ CPE: Common Platform Enumeration, part of SCAP standard, a structured naming scheme
  used to identify information technology systems, platforms, and packages.
+ CVE: Common Vulnerabilities and Exposures, part of SCAP standar, an enumeration
  for publicly known information security vulnerabilities.
+ CVSS:
+ CWE
+ DataStream
+ FIPS
+ MITRE
+ NIST
+ NVD
+ OCIL: Open Checklist Interactive Language, part of SCAP standard, a language
  providing standard way of querying a human user about the state of endpoint.
+ OVAL: Open Vulnerability and Assessment Language, part of SCAP standard, declarative
  language for making logical assetions about the state of endpoint system.
+ SCE: Sript Check Engine: SCAP extension to allow script execution from SCAP policy.
  That might be useful during rapid policy development as scripts are easier to write
  than OVAL.
+ SDS
+ SACM
+ SCAP
+ SWID
+ TMSAD
+ XCCDF: eXtensible Configuration Checklist Description Format, part of SCAP standard,
  a language to express, organize, and manage security policies. Basic building block
  of security policy.

# Security Policies
+ There is huge variety of policies
+ How to choose a policy?
+ Open development of security policies

## All Public SCAP Policies
+ SSG: SCAP-Security-Guide
+ DISA STIG: Secure Technical Implementation Guidelines
+ USGCB:
+ NVD database
+ CIS benchmarks
+ SEC POD repo? http://www.scaprepo.com/

### SSG Guides
+ State of the development for various guides.
+ RHEL-6 Policies
 + DISA STIG upstream
 + ...
+ RHEL-7 Policies
 + DISA STIG upstream
 + ...
+ Fedora
+ Firefox
+ JRE

## Open Development of Security Policies
+ Why collaborate?
+ How to get started?

## Tailoring Security Policy
+ What is it?
+ Why would you do it?
+ file format?

# Tools
+ What open source tools do we have?

## OpenSCAP base
+ Project homepage

## OpenSCAP Daemon
+ Project homepage

## SCAP-Workbench
+ Project homepage

## SCAPtimony
+ Project homepage

## OSCAP-Anaconda-Addon
+ Project homepage

## Related projects
+ pre-upgrade assistant
+ access insights
+ foreman integration

# Resources

## Support
+ How to get support for OpenSCAP projects

## Tutorial & Videos

### Getting Started with OpenSCAP
+ Get oscap
+ Get SSG policy
+ Run first scan

### Use SCAP Workbench for tailoring

### How to run a vulnerability scan

## Documentation
+ Mix of
  + Chapter 'OpenSCAP' from RHEL7 Security Guide
  + open-scap upstream docs

## News and blogs (perhaps google plus)

## Contribute

## About Team
